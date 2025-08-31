import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("HUGGINGFACE_API_KEY")

# Use FLUX.1 [schnell] model endpoint
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-schnell"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def generate_image(prompt, output_file="output.png"):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        with open(output_file, "wb") as f:
            f.write(response.content)
        print(f"Image saved as {output_file}")
    else:
        print("Error:", response.status_code, response.text)

if __name__ == "__main__":
    prompt = """
    Advertising photography of a black and white supplement bottle labeled "ELV Control", floating in the air surrounded by fresh natural elements such as nopal, spirulina seaweed powder, pieces of tejocote root, pieces of pineapple and apple, minimalist white background, modern sans serif text, bold product branding, slight isometric tilt for dynamic composition, soft studio lighting with subtle shadows to give depth, fresh and health-oriented visual style, vibrant green accents with hints of red and blue, high-resolution commercial aesthetic, photographed with a Canon EOS R5, 85mm f/1.8 lens, neutral color correction, contrast and sharpness. 8, neutral color gradation with high contrast and clarity
    """
    generate_image(prompt, "elv2.png")
