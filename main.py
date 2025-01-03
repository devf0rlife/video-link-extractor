import subprocess
import re
import os
import argparse
import sys
from urllib.parse import urlparse


def fetch_with_wget(url: str):
    output_file = "output.html"
    command = ['wget', '--user-agent=Mozilla/5.0', '-O', output_file, url]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError:
        print(f"Error fetching the URL: {url}")
        sys.exit(1)

    with open(output_file, "r") as file:
        content = file.read()

    os.remove(output_file)
    return content


def extract_video_url(html_content: str):
    video_match = re.search(r'([^"]*\.mp4)', html_content)
    return video_match.group(1) if video_match else None


def extract_thumb_url(html_content: str):
    video_match = re.search(r'([^"]*\.jpg)', html_content)
    return video_match.group(1) if video_match else None


def main():
    parser = argparse.ArgumentParser(
        description="Fetch and extract video URL from a webpage.")
    parser.add_argument("url", help="URL of the webpage to fetch.")
    args = parser.parse_args()

    url = args.url
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    html_content = fetch_with_wget(url)

    if domain == "nudetab.com":
        video_url = []
        link = extract_video_url(html_content)
        thumb = extract_thumb_url(html_content)
        video_url.append(link)
        video_url.append(thumb)
    else:
        video_url = extract_video_url(html_content)

    if video_url:
        print(video_url)
    else:
        print("No video URL found")


if __name__ == '__main__':
    main()
