import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from dotenv import load_dotenv
import pickle

# Load environment variables
load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

# Paths loaded from environment
CLIENT_SECRET_FILE = os.getenv("CLIENT_SECRET_FILE", "client_secret.json")
TOKEN_FILE = os.getenv("TOKEN_FILE", "token.pickle")

def upload_video(video_path, title, description="", thumbnail_path=None):
    creds = None

    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print("[Error] Could not refresh credentials:", e)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(TOKEN_FILE, "wb") as token:
            pickle.dump(creds, token)

    youtube = build("youtube", "v3", credentials=creds)

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": ["AI", "AutoCreator", "Python"]
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    media_file = MediaFileUpload(video_path, mimetype="video/*", resumable=True)
    upload_request = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media_file
    )
    response = upload_request.execute()
    print(f"[✓] Video uploaded: https://www.youtube.com/watch?v={response['id']}")

    # Upload thumbnail if provided
    if thumbnail_path and os.path.exists(thumbnail_path):
        youtube.thumbnails().set(
            videoId=response["id"],
            media_body=MediaFileUpload(thumbnail_path)
        ).execute()
        print("[✓] Thumbnail uploaded.")

if __name__ == "__main__":
    upload_video("media/final_video.mp4", "Sample Title", "Sample Description")
