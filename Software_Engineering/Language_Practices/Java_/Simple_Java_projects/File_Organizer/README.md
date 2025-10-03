# 📂 Java File Organizer (CLI)

A simple **command-line file organizer** written in Java.  
This program scans a given folder, detects file types by extension, and automatically moves them into categorized subfolders (`Images`, `Documents`, `Videos`, `Music`, `Others`).  

---

## 🚀 Features
- ✅ Organizes files by type  
- ✅ Automatically creates folders (`Images`, `Documents`, `Videos`, `Music`, `Others`)  
- ✅ Prevents folder clutter  
- ✅ Works on Linux, macOS, and Windows  

---

## 📦 Requirements
- Java 8 or higher  
- A directory with mixed file types (e.g., `Downloads`)  

---

## 🔧 Build & Run

### 1. Compile the program
```bash
javac FileOrganizer.java

Run the program
java FileOrganizer <directory-path>


Example:

java FileOrganizer ~/Downloads

📌 Example Usage

Before running:

Downloads/
  - photo1.jpg
  - movie.mp4
  - report.pdf
  - song.mp3


After running:

Downloads/
  ├── Images/
  │   └── photo1.jpg
  ├── Videos/
  │   └── movie.mp4
  ├── Documents/
  │   └── report.pdf
  ├── Music/
  │   └── song.mp3
  └── Others/

🛠️ Future Improvements

Allow custom categories via a config file

Add logging for moved files

Recursive organization (include subfolders)

📜 License

This project is open-source and available under the MIT License
.


