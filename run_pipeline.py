from idea_gen import get_latest_idea_and_script
from generate_audio import generate_audio
from generate_image import generate_image
from generate_video import generate_video
# from upload_video import upload_video  # <- Comment this out
import os
import shutil

def clean_media_folder():
    media_dir = "media"
    if os.path.exists(media_dir):
        for filename in os.listdir(media_dir):
            file_path = os.path.join(media_dir, filename)
            try:
                os.remove(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")

clean_media_folder()

if __name__ == '__main__':
    idea, script = get_latest_idea_and_script()

    if not idea or not script:
        print("No new ideas found.")
        exit()

    print("Generating audio...")
    generate_audio(script)

    print("Generating image...")
    generate_image(idea)

    print("Generating video...")
    generate_video("media/image.jpg", "media/audio.mp3", "media/final_video.mp4")

    # Skipping YouTube upload for now
    print("[✔] Video generated. Review it before uploading.")
