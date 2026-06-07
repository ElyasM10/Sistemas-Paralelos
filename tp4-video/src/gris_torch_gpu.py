import cv2
import torch
import time
import os

device = torch.device("cuda")

VIDEO_PATH = "../videos/video.mp4"
OUTPUT_PATH = "../resultados/gris_torch_gpu.mp4"

# Crear carpeta resultados si no existe
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

video = cv2.VideoCapture(VIDEO_PATH)

fps = video.get(cv2.CAP_PROP_FPS)
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer = cv2.VideoWriter(
    OUTPUT_PATH,
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height),
    False
)

frames = 0

inicio = time.time()

while True:

    ret, frame = video.read()

    if not ret:
        break

    tensor = torch.tensor(
        frame,
        dtype=torch.float32,
        device=device
    )

    gris = (
        0.299 * tensor[:, :, 2]
        + 0.587 * tensor[:, :, 1]
        + 0.114 * tensor[:, :, 0]
    )

    gris = gris.cpu().numpy().astype("uint8")

    writer.write(gris)

    frames += 1

torch.cuda.synchronize()

fin = time.time()

video.release()
writer.release()

tiempo_total = fin - inicio

print(f"Frames procesados: {frames}")
print(f"Tiempo total: {tiempo_total:.2f} segundos")
print(f"FPS efectivos: {frames/tiempo_total:.2f}")