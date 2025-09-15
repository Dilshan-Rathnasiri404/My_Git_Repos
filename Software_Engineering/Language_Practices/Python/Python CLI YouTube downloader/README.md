# 🎬 Python CLI YouTube Downloader

A simple **Python command-line tool** to download videos from YouTube using `yt-dlp`.  
Works on **Linux, macOS, and Windows**. Great for Linux users who prefer CLI tools.

---



## 📦 Requirements

- **Python 3.6+**  
  Check if Python is installed:
  ```bash
  python3 --version
yt-dlp library

bash
Copy code
pip install yt-dlp



🚀 Usage
Clone this repository:

bash
Copy code
git clone https://github.com/Dilshan-Rathnasiri404/VideoDownloaderPython.git
cd VideoDownloaderPython
Run the downloader:

bash
Copy code
python3 youtube_downloader.py <video_url>
Replace <video_url> with the link of the video you want to download.




📝 Example
bash
Copy code
python3 youtube_downloader.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
Output:

less
Copy code
Downloading video from: https://www.youtube.com/watch?v=dQw4w9WgXcQ
[youtube] dQw4w9WgXcQ: Downloading webpage
[youtube] dQw4w9WgXcQ: Downloading video info
[download] Destination: Rick Astley - Never Gonna Give You Up.mp4
✅ Download complete!
📂 Project Structure
bash
Copy code
Python-YouTube-Downloader/
│
├── youtube_downloader.py   # Main Python script
└── README.md               # Documentation




⚠️ Notes
Works offline after installing yt-dlp.

Downloads best available video + audio quality by default.

Always respect the YouTube Terms of Service. Use only for educational purposes or your own videos.




🛠️ Future Improvements
Add audio-only download option

Add custom output folder

Add progress bar for large videos

Add support for batch downloads from playlist URLs
