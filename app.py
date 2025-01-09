from flask import Flask, request, send_from_directory
import os
import zipfile
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Direktori untuk menyimpan file sementara
UPLOAD_FOLDER = '/tmp/uploads'
TARGET_FOLDER = '/usr/local/etc/xray/config'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return send_from_directory('.', 'restore.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    if file and file.filename.endswith('.zip'):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Extract the zip file
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(UPLOAD_FOLDER)

        # Move extracted files to target directory
        target_file_path = os.path.join(TARGET_FOLDER, '04_inbounds.json')
        extracted_file_path = os.path.join(UPLOAD_FOLDER, '04_inbounds.json')

        if os.path.exists(extracted_file_path):
            if os.path.exists(target_file_path):
                os.remove(target_file_path)
            os.rename(extracted_file_path, target_file_path)
            return "File uploaded and replaced successfully"
        else:
            return "04_inbounds.json not found in ZIP", 400
    else:
        return "Invalid file type. Only ZIP files are allowed", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
  
