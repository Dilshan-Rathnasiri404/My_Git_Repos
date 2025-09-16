📥 C++ YouTube Downloader

A simple command-line tool written in C++ that downloads YouTube videos by calling yt-dlp
 in the background.
This program is designed for Linux users who want a fast and minimal video downloader they can run from the terminal.




🚀 Features

✅ Lightweight and fast — compiled C++ binary

✅ Cross-platform (works on Linux, macOS, Windows with yt-dlp installed)

✅ Minimalistic — just pass the YouTube URL and download



🛠️ Requirements

Make sure you have yt-dlp installed:

sudo apt update && sudo apt install yt-dlp -y


You also need g++ to compile the program:

sudo apt install g++ -y




📦 Installation

Clone the repository and compile:

git clone https://github.com/<your-username>/cpp-youtube-downloader.git
cd cpp-youtube-downloader
g++ youtube_downloader.cpp -o youtube_downloader





▶️ Usage
./youtube_downloader "<YouTube-Video-URL>"

Example:
./youtube_downloader "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

📂 Project Structure
cpp-youtube-downloader/
├── youtube_downloader.cpp
└── README.md





💡 Notes

This project does not directly parse YouTube — it uses yt-dlp for all the heavy lifting.

You can pass any yt-dlp-supported URL (YouTube, Vimeo, Twitter, etc.).




📜 License

This project is released under the MIT License. You are free to use, modify, and distribute it.
