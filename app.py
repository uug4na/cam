from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'message': 'No image file provided.'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'message': 'No selected file.'}), 400

    filename = secure_filename(image.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(filepath)

    return jsonify({'message': 'Image uploaded successfully.', 'filename': filename}), 200

if __name__ == '__main__':
    app.run(debug=True)
