#include <iostream>
#include <cstdlib>
#include <string>
#include <filesystem>

using namespace std;

bool checkYtDlpInstalled() {
    int result = system("yt-dlp --version > /dev/null 2>&1");
    return result == 0;
}

int main(int argc, char* argv[]) {
    if (!checkYtDlpInstalled()) {
        cerr << "Error: yt-dlp is not installed or not found in PATH." << endl;
        cerr << "Please install it using: sudo apt install yt-dlp" << endl;
        return 1;
    }

    if (argc < 2) {
        cerr << "Usage: " << argv[0] << " <URL> [--audio-only] [--quality <res>] [--output-folder <folder>]" << endl;
        return 1;
    }

    string url = argv[1];
    string command = "yt-dlp ";
    string outputFolder = "."; // default current directory
    string quality = "bestvideo+bestaudio";

    for (int i = 2; i < argc; ++i) {
        string arg = argv[i];
        if (arg == "--audio-only") {
            quality = "bestaudio";
        } else if (arg == "--quality" && i + 1 < argc) {
            quality = "bestvideo[height=" + string(argv[i + 1]) + "]+bestaudio";
            i++; // skip next argument as we used it
        } else if (arg == "--output-folder" && i + 1 < argc) {
            outputFolder = argv[i + 1];
            i++;
        }
    }

    // Ensure output folder exists
    if (!filesystem::exists(outputFolder)) {
        filesystem::create_directories(outputFolder);
    }

    command += "-f \"" + quality + "\" -o \"" + outputFolder + "/%(title)s.%(ext)s\" " + url;

    cout << "Running command: " << command << endl;
    int result = system(command.c_str());

    if (result == 0) {
        cout << "✅ Download completed successfully!" << endl;
    } else {
        cerr << "❌ Download failed. Please check the URL or try again." << endl;
    }

    return result;
}
