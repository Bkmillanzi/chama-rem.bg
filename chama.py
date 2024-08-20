from flask import Flask, request, send_file
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)  # This allows all origins

@app.route('/process-image', methods=['POST'])
def process_image():
    file = request.files['image']
    input_path = 'input.jpg'
    output_path = 'output.png'
    file.save(input_path)

    command = [
        'rembg', 'i',
        '-m', 'u2net_human_seg',
        '-x', '{"model_path": "C:/Users/USER/.u2net/u2net.onnx"}',
        input_path, output_path
    ]
    subprocess.run(command, check=True)

    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

