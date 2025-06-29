from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.secret_key = 'your_secret_key'

# Configure upload and model paths
UPLOAD_FOLDER = 'static/uploads'
MODEL_PATH = 'cheque_verification_model.h5'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif','tif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load pre-trained model
model = load_model(MODEL_PATH)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def preprocess_image(file_path):
    # Open the image
    img = Image.open(file_path)
    
    # Resize to match model's expected input
    img = img.resize((224, 224))
    
    # Convert to array
    img_array = img_to_array(img)
    
    # Normalize pixel values
    img_array = img_array / 255.0
    
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    
    return img_array

def predict_cheque(file_path):
    # Preprocess the image
    processed_image = preprocess_image(file_path)
    
    # Make prediction
    prediction = model.predict(processed_image)[0][0]
    
    # Convert to binary classification result
    result = 'Genuine' if prediction > 0.5 else 'Forged'
    
    return result

# Route for file upload
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    
    file = request.files['file']
    
    if file.filename == '':
        return 'No file selected', 400
    
    if file and allowed_file(file.filename):
        # Save the file
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        
        # Predict cheque authenticity
        try:
            result = predict_cheque(filename)
            return result
        except Exception as e:
            return 'Error processing image', 500
    
    return 'Invalid file type', 400

# Route for serving frontend
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)