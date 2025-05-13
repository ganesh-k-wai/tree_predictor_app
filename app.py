from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

PREDICTION_URL = "https://customvisionbygk-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/0d8bf1c5-f770-4cb5-b916-eb6bdafa97ff/classify/iterations/Tree_Classify/image"
PREDICTION_KEY = "MDcLFU9MAFYTT7wjZyPzLdUFrLKYkdCpw9A2bFAiiLyBt0EMxMvmJQQJ99BEACGhslBXJ3w3AAAIACOGCbHP"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    image = request.files['image']
    headers = {
        'Prediction-Key': PREDICTION_KEY,
        'Content-Type': 'application/octet-stream'
    }
    response = requests.post(PREDICTION_URL, headers=headers, data=image.read())
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({'error': 'Prediction failed', 'details': response.text}), 500

if __name__ == '__main__':
    app.run(debug=True)