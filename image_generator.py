import replicate
import os
from dotenv import load_dotenv

class ImageGenerator:
    def __init__(self):
        load_dotenv()
        # Make sure to set REPLICATE_API_TOKEN in your .env file
        self.api_token = os.getenv('REPLICATE_API_TOKEN')
        
    def generate_image(self, prompt):
        try:
            input_params = {
                "prompt": f"youtube thumbnail, {prompt}",
                "guidance": 3.5,
                "width": 1920,  # Set desired width
                "height": 1080   # Set desired height
            }
            
            print("Starting image generation...")
            output = replicate.run(
                "black-forest-labs/flux-dev",
                input=input_params
            )
            
            # Save the image
            for index, item in enumerate(output):
                filename = f"output_{index}.webp"
                with open(filename, "wb") as file:
                    file.write(item.read())
                print(f"Saved image as {filename}")
                
            return True, "Image generated successfully"
            
        except Exception as e:
            return False, f"Error: {str(e)}"