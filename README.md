# Flask Chatbot with Google Generative AI

## Overview
This project is a Flask-based chatbot that integrates Google Generative AI (Gemini-2.0-Flash) to provide conversational responses. It supports both text-based chat and image processing.

## Features
- Interactive chat with AI using Google GenAI API
- Session-based conversation history
- Image processing to generate AI responses based on uploaded images
- Secure API key management using environment variables

## Technologies Used
- **Flask**: Web framework for Python
- **Google Generative AI**: Gemini-2.0-Flash model
- **PIL (Pillow)**: Image processing
- **Requests**: Handling HTTP requests
- **dotenv**: Loading environment variables

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/vikky2810/Python_ImageChat.git
   cd Python_ImageChat
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Set up environment variables:
   - Create a `.env.local` file in the root directory.
   - Add your Google API key:
     ```ini
     GOOGLE_API_KEY=your_api_key_here
     ```

5. Run the application:
   ```sh
   python app.py
   ```

6. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## API Endpoints
| Endpoint              | Method | Description |
|----------------------|--------|-------------|
| `/`                  | GET    | Renders the chat interface |
| `/get_conversation`  | GET    | Retrieves the conversation history |
| `/chat`              | POST   | Sends user input to AI and receives a response |

## Usage
1. Open the web interface.
2. Enter a message in the chat box and submit.
3. The AI will generate a response based on previous messages.
4. Upload an image to analyze its content.

## Environment Variables
The project uses environment variables stored in a `.env.local` file. The required variable is:
- `GOOGLE_API_KEY` - Your Google GenAI API key

## Notes
- Ensure you have an active internet connection to interact with the AI model.
- API key security is crucial; do not expose it publicly.
- You can change the AI model by modifying `MODEL_ID` in `app.py`.


## Author
[Vikram Kamble](https://github.com/vikky2810)

