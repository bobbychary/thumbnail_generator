# Save this exactly as prompt_enhancer.py
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
    full_prompt = f"""You are the world's leading art expert, knowledgable in the entire corpus of human art and techniques used in them. Take the following input and turn it into a sophisticated image prompt for a youtube thumbnail, sticking closely to the original provided idea. This will be using short, concise highly creative and aesthetic language borrowing from a wide corpus of visual language and art history. The images can create text too if needed when the user requests or in context, in double quotes. Do not preface or introduce the prompt, it is solely meant for machine consumption, follow the examples below. Do not add ".", only commas

Here are some examples:

INPUT: Greek statue figure, green eyes, financial data background
OUTPUT: A digital artwork of a stylized male figure resembling a Greek statue, with glowing green eyes and an open mouth expressing surprise or shock, white hair and beard, front-facing, with a background featuring graphical elements associated with financial data, two text boxes on the upper left and right of the image showing "Views" with a green upward arrow and the number "394.1K", and "Estimated revenue" with a green upward arrow and the currency figure "$5,941.1", respectively, lines resembling a rising graph or stock market data in light blue behind the figure, scattered green money bills with one hundred dollar denomination floating around the figure, with a dark green to black gradient backdrop, the vibe of the image is surreal and related to financial growth or success

INPUT: serious man with beard, stylized brain, social media icons, surreal digital background
OUTPUT: a man with a beard and a serious expression, a stylized human brain held in two hands at the left side of the image, two cables plugged into the brain with icons at their ends representing social media platforms, one icon labeled "hub" colored in gold with a black base and resembling the logo of a popular adult website, a second icon colored in pink and mint green with a music note symbol resembling the logo of TikTok, the background is blurred with blue and yellow tones, the image has an overall surreal and digitally manipulated appearance

INPUT: dramatic digital art, stern man, financial crisis, burning Wall Street, stock market crash
OUTPUT: A digitally created image, a stern-looking man in a suit with a scowling expression, flames and burning buildings in the background marked "WALL ST", scattered US dollar bills in the foreground, images of the New York Stock Exchange and trading ticker screens on fire, a partially visible newspaper with the headline "The New York Times" and text "STOCKS PLUNGE 588 POINTS, A DROP OF 22%", "26.3 MILLION VOLUME NEARLY DOUBLES RECORD", "WALL S" sign with a burning effect, digital art, dramatic representation of a financial crisis

INPUT: digital map composite, Abraham Lincoln, USA and Mexico, cracked effect
OUTPUT: A digital composite image with a textured background resembling a map, featuring a portrait of Abraham Lincoln on the left, the map is colored in two distinct shades with the northern part indicating the USA in gray and labeled with a flag icon and "USA" text in capital letters, the southern part indicating Mexico in red and labeled with a flag icon and "MEXICO" text in capital letters, both countries' names are displayed in bold white font, the image is artistically cracked to enhance a historical or thematic effect

INPUT: promotional graphic, man with beard, orange and yellow theme, dollar signs, social media icons, "EYECATCHING THUMBNAIL" text, "GraphicDrive.psd" label, $5 price tag
OUTPUT: A promotional graphic for a service or product featuring a man with a beard looking sideways, orange and yellow color theme, dollar signs and money graphics suggesting a price or cost, social media icons such as the YouTube play button, bold text in the center reading "EYECATCHING THUMBNAIL" suggesting the subject of the promotion, smaller text at the top right saying "GraphicDrive.psd" indicating the name of the template or service, and a '5$' price tag graphic in the top left corner indicating affordability

INPUT: split facial expression, distressed and smiling, dark blue and green background, viewership highs and lows
OUTPUT: A man with a split facial expression, left side shows a distressed look with hand on head, right side smiles broadly, the background is split into two contrasting colors, dark blue on the left and green on the right, text on the left reads "VIEWS 1" with a red down arrow, text on the right reads "VIEWS 1.4M" with a green up arrow, a concept depicting the highs and lows of content viewership

INPUT: {input_prompt}
OUTPUT:"""
    
    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"