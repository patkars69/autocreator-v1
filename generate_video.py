import subprocess

def generate_video(image_path, audio_path, output_path):
    command = [
        "ffmpeg",
        "-y",
        "-loop", "1",
        "-i", image_path,
        "-i", audio_path,
        "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2",  # 👈 Ensures even width/height
        "-c:v", "libx264",
        "-tune", "stillimage",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",
        output_path
    ]

    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print("[FFmpeg ERROR]")
        print(result.stderr)
    else:
        print("✅ Video created:", output_path)

if __name__ == "__main__":
    generate_video("media/image.jpg", "media/audio.mp3", "media/final_video.mp4")
