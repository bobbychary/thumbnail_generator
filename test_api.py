import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = 'AIzaSyDAQd8j1iMQaB6Z4jVm-mCiGYdGeRw9ziI'  # Your API key

# Configure API key
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel('gemini-pro')

def test_connection():
    try:
        response = model.generate_content("Hello, this is a test prompt")
        print("Connection successful!")
        print("Response:", response.text)
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    test_connection()