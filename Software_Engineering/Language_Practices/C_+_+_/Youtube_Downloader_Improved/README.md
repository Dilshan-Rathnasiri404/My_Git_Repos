# 🎥 C++ YouTube Downloader (CLI)

A lightweight **command-line YouTube downloader** written in C++ that uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) under the hood.  
Supports downloading full videos, audio-only, custom quality (e.g., 1080p), and saving to a custom output folder.

---

## 🚀 Features
- ✅ **Download full videos or audio-only**
- ✅ **Choose video resolution** (e.g., 1080p, 720p)
- ✅ **Custom output folder**
- ✅ **Automatic folder creation**
- ✅ **Checks if `yt-dlp` is installed**
- ✅ **Works on Linux / macOS / Windows**

---

## 📦 Prerequisites

Make sure `yt-dlp` is installed on your system:

```bash
sudo apt update && sudo apt install yt-dlp   # For Debian/Ubuntu/Kali


For macOS:

brew install yt-dlp


For Windows:

Download yt-dlp.exe from yt-dlp releases

Add it to your PATH.


🔧 Build Instructions

Compile the C++ file:

g++ youtube_downloader.cpp -o youtube_downloader


🎯 Usage
./youtube_downloader <URL> [options]

Options:
Option	Description
--audio-only	Download audio only (mp3/m4a format)
--quality <res>	Specify resolution (e.g., 1080, 720)
--output-folder <folder>	Choose output folder (creates it if missing)
📌 Examples
1. Download full video
./youtube_downloader "https://youtube.com/watch?v=dQw4w9WgXcQ"

2. Download audio only
./youtube_downloader "https://youtube.com/watch?v=dQw4w9WgXcQ" --audio-only

3. Download in 1080p
./youtube_downloader "https://youtube.com/watch?v=dQw4w9WgXcQ" --quality 1080

4. Save to custom folder
./youtube_downloader "https://youtube.com/watch?v=dQw4w9WgXcQ" --output-folder Downloads


🛠️ Error Handling

If yt-dlp is not installed, the program will show an error message.

Invalid URLs will trigger a failure message.


📜 License

This project is open-source and available under the MIT License
.
