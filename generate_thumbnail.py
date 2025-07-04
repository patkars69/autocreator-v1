from PIL import Image
import os

def generate_thumbnail(input_path="media/image.jpg", output_path="media/thumbnail.jpg", size=(1280, 720)):
    if not os.path.exists(input_path):
        print(f"Image not found: {input_path}")
        return
    img = Image.open(input_path)
    img = img.resize(size, Image.ANTIALIAS)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path)
    print(f"Thumbnail saved to {output_path}")

if __name__ == "__main__":
    generate_thumbnail()
