import cv2

VIDEO_PATH = "../videos/video.mp4"

video = cv2.VideoCapture(VIDEO_PATH)

if not video.isOpened():
    print("Error al abrir el video")
    exit()

fps = video.get(cv2.CAP_PROP_FPS)
frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"Resolución: {width}x{height}")
print(f"FPS: {fps}")
print(f"Frames: {frames}")

video.release()