import cv2
import datetime

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f"captured_image_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png", frame)
    cap.release()

capture_image()