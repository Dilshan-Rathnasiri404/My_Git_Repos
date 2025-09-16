#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <YouTube URL>\n";
        return 1;
    }

    std::string url = argv[1];
    std::string command = "yt-dlp \"" + url + "\"";

    std::cout << "Downloading video from: " << url << std::endl;

    int result = std::system(command.c_str());
    if (result == 0) {
        std::cout << "✅ Download complete!" << std::endl;
    } else {
        std::cerr << "❌ Failed to download video." << std::endl;
    }

    return 0;
}
