import subprocess
import re
def fetch_with_wget(url: str):
    output_file = "output.html"
    command = ["wget", '--user-agent="Mozilla/5.0"','--refere="mydesi2.net"',"-O", output_file, url]
    subprocess.run(command)
    with open(output_file, "r") as file:
        return file.read()
    com = ["rm output.html"]
    subprocess.run(com)

url = ""
html_content = fetch_with_wget(url)

# Extract video URL
video_match = re.search(r'source src="([^"]*\.mp4)"', html_content)
if video_match:
    video_url = video_match.group(1)
    print("Video URL:", video_url)
else:
    print("No video URL found")

# Extract poster image URL
poster_match = re.search(r'"poster":\s*"([^"]*\.jpg)\??[^"]*"', html_content)
if poster_match:
    poster_url = poster_match.group(1)  # This will capture up to .jpg only
    print("Poster URL:", poster_url)
else:
    print("No poster URL found")