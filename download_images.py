import os
import requests
from duckduckgo_search import DDGS

def download_image(query, save_path='media/image.jpg'):
    os.makedirs('media', exist_ok=True)
    with DDGS() as ddgs:
        results = ddgs.images(query, max_results=1)
        for r in results:
            image_url = r["image"]
            try:
                img_data = requests.get(image_url).content
                with open(save_path, 'wb') as f:
                    f.write(img_data)
                print(f"Image downloaded to {save_path}")
                return save_path
            except Exception as e:
                print(f"Failed to download image: {e}")
                return None
    print("No image found.")
    return None

if __name__ == '__main__':
    from idea_gen import get_latest_idea
    idea = get_latest_idea()
    download_image(idea)
