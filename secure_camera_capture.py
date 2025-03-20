import cv2
import datetime
import os
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

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

capture_image()