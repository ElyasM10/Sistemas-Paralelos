import cv2
import time

VIDEO_PATH = "../videos/video.mp4"

video = cv2.VideoCapture(VIDEO_PATH)

inicio = time.time()

frames = 0

while True:
    ret, frame = video.read()

    if not ret:
        break

    frames += 1

fin = time.time()

video.release()

print(f"Frames leídos: {frames}")
print(f"Tiempo lectura: {fin - inicio:.2f} segundos")
print(f"FPS efectivos: {frames/(fin-inicio):.2f}")