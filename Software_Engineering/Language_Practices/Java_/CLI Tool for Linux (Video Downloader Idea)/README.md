# 🎬 Java CLI YouTube Video Downloader

A simple **Java command-line tool** for downloading videos from YouTube using **yt-dlp**.  
Designed for Linux users who prefer CLI applications.

---

## ⚡ Features
- Download videos directly from YouTube URLs  
- Works entirely in the terminal (no GUI needed)  
- Cross-platform (Linux, Windows, macOS — with Java installed)  
- Easy to extend with additional features (audio-only, output folder, etc.)

---

## 📦 Requirements
1. **Java JDK** installed  
   Check Java version:
   ```bash
   java -version
yt-dlp installed
On Linux (Debian/Kali/Ubuntu):

bash
Copy code
sudo apt update
sudo apt install yt-dlp -y
Or via Python:

bash
Copy code
pip install yt-dlp
🚀 Installation & Setup
Clone this repository:

bash
Copy code
git clone https://github.com/Dilshan-Rathnasiri404/VideoDownloader.git
cd VideoDownloader
Compile the Java program:

bash
Copy code
javac LinuxVideoDownloader.java
Run the downloader with a YouTube URL:

bash
Copy code
java LinuxVideoDownloader <youtube_url>


📝 Example Usage
bash
Copy code
java LinuxVideoDownloader https://www.youtube.com/watch?v=dQw4w9WgXcQ
Sample Output:

csharp
Copy code
[youtube] Extracting URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
[youtube] dQw4w9WgXcQ: Downloading webpage
...
[download] Destination: Rick Astley - Never Gonna Give You Up.mp4
[download] 100% of 3.50MiB in 00:03
✅ Download complete!


🛠️ Project Structure
kotlin
Copy code
VideoDownloader/
│
├── LinuxVideoDownloader.java   # Main Java program
├── README.md                   # Documentation (this file)
└── .gitignore                  # Optional: ignore .class files



⚠️ Notes & Disclaimer
This tool is for educational purposes only.

Downloading videos from YouTube may violate their Terms of Service.

Use it responsibly — only download videos you own or are allowed to use.



🚀 Future Improvements
Add output folder selection

Add audio-only download option

Add progress bar and colored terminal messages

Support for other video platforms
