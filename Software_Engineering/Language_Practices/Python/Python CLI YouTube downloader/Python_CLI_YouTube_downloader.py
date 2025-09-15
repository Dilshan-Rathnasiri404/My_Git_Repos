import sys
from yt_dlp import YoutubeDL

def download_video(url):
    ydl_opts = {
        'format': 'best',   # Best quality video + audio
        'outtmpl': '%(title)s.%(ext)s',  # Save with video title as filename
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def main():
    if len(sys.argv) != 2:
        print("Usage: python youtube_downloader.py <video_url>")
        sys.exit(1)

    url = sys.argv[1]
    print(f"Downloading video from: {url}")
    download_video(url)
    print("✅ Download complete!")

if __name__ == "__main__":
    main()
