from flask import Flask, request, jsonify, render_template
from google import genai
from google.genai import types
from PIL import Image
import requests
import io
import os
from dotenv import load_dotenv

# Load environment variables from .env.local
load_dotenv('.env.local')

app = Flask(__name__)

# Initialize the Google Gen AI client
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')  # Get API key from environment
if not GOOGLE_API_KEY:
    raise ValueError("No GOOGLE_API_KEY found in environment variables.")

client = genai.Client(api_key=GOOGLE_API_KEY)

# Choose the model
MODEL_ID = "gemini-2.0-flash"  # You can change this to another model if needed

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message')
    image_file = request.files.get('image_file')

    if image_file:
        # Process the uploaded image
        response = process_image(image_file)
        return jsonify({"response": response})

    # Normal chat response
    response = generate_response(user_message)
    return jsonify({"response": response})

def generate_response(message):
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=message
    )
    return response.text

def process_image(image_file):
    # Open the image file
    image = Image.open(image_file)

    # Generate a prompt based on the image
    prompt = "Describe the content of this image."
    
    # Send the image and prompt to the model
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[image, prompt]
    )
    return response.text

if __name__ == '__main__':
    app.run(debug=True)