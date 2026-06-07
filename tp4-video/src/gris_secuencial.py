import cv2
import time
import os

VIDEO_PATH = "../videos/video.mp4"
OUTPUT_PATH = "../resultados/gris_secuencial.mp4"

# Crear carpeta resultados si no existe
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

video = cv2.VideoCapture(VIDEO_PATH)

if not video.isOpened():
    raise Exception("No se pudo abrir el video")

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

inicio_total = time.time()

while True:

    ret, frame = video.read()

    if not ret:
        break

    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    writer.write(gris)

    frames += 1

fin_total = time.time()

video.release()
writer.release()

tiempo_total = fin_total - inicio_total

print(f"Frames procesados: {frames}")
print(f"Tiempo total: {tiempo_total:.2f} segundos")
print(f"FPS efectivos: {frames/tiempo_total:.2f}")