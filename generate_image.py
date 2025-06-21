import os
import requests
from duckduckgo_search import ddg_images
from PIL import Image
from io import BytesIO

def generate_image(prompt):
    safe_prompt = prompt.replace('"', '').replace(":", "").replace("?", "")
    print(f"[Image Gen] Searching for image with prompt: {safe_prompt}")

    results = ddg_images(safe_prompt, max_results=1)
    if not results:
        print("[Error] No image results found.")
        return

    image_url = results[0]['image']
    print(f"[Image Gen] Downloading image from: {image_url}")

    try:
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))

        media_path = "media"
        os.makedirs(media_path, exist_ok=True)

        image_path = os.path.join(media_path, "image.jpg")
        img.convert("RGB").save(image_path, "JPEG")
        print(f"[Image Gen] Saved image to: {image_path}")

    except Exception as e:
        print(f"[Error] Failed to download/save image: {e}")

