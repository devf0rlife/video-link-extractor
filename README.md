
# Video URL Extractor Script

This script is designed to fetch a webpage, extract its HTML content, and search for a video URL (specifically `.mp4` file links). It uses the `wget` command-line tool to fetch the page content and `regex` to extract the video URL.

## Requirements

- Python 3.x
- `wget` command-line tool installed on your system
- Internet access to fetch the webpage

## Installation

1. Ensure that Python 3.x is installed. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/).
2. Make sure `wget` is installed on your system. You can verify this by running the following in your terminal:
   ```bash
   wget --version
   ```
   If `wget` is not installed, you can install it using your package manager:
   - On Ubuntu/Debian: `sudo apt install wget`
   - On macOS: `brew install wget`
   - On Windows: Install it from [https://eternallybored.org/misc/wget/](https://eternallybored.org/misc/wget/).

## Usage

To use the script, run the following command:

```bash
python main.py <url>
```

Replace `<url>` with the URL of the webpage you wish to fetch and extract the video URL from.

### Example

```bash
python main.py https://example.com
```

If a `.mp4` video URL is found on the webpage, it will be printed in the terminal:

```bash
Video URL: http://example.com/path/to/video.mp4
```

If no video URL is found, the script will inform you with:

```bash
No video URL found
```

## Functionality

- **Fetches webpage content**: The script uses `wget` with a custom user-agent to fetch the HTML content of the provided URL.
- **Extracts video URL**: It looks for `.mp4` links in the HTML content using regular expressions.
- **Deletes temporary file**: After extracting the video URL, the script deletes the temporary HTML file.

## Troubleshooting

- **Error fetching the URL**: If the URL fetch fails, the script will exit with an error message. Ensure that `wget` is installed and the URL is correct.
- **No video found**: If no `.mp4` link is found, the script will print `No video URL found`.

## License

This script is provided as-is. Feel free to modify and use it as needed for your personal or professional projects.
