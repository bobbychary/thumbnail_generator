import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key and configure
load_dotenv()
api_key = 'AIzaSyDAQd8j1iMQaB6Z4jVm-mCiGYdGeRw9ziI'
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel('gemini-pro')

def enhance_prompt(input_prompt):
    # Your existing prompt template
    full_prompt = f"""You are the world's leading art expert, knowledgable in the entire corpus of human art and techniques used in them. Take the following input and turn it into a sophisticated image prompt for a youtube thumbnail, sticking closely to the original provided idea. This will be using short, concise highly creative and aesthetic language borrowing from a wide corpus of visual language and art history. The images can create text too if needed when the user requests or in context, in double quotes. Do not preface or introduce the prompt, it is solely meant for machine consumption, follow the examples below. Do not add ".", only commas

    INPUT: {input_prompt}
    OUTPUT:"""

    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Quick test
if __name__ == "__main__":
    test_prompt = "cat with glasses"
    result = enhance_prompt(test_prompt)
    print("Enhanced prompt:", result)