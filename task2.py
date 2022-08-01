import requests
import validators
from moviepy.editor import VideoFileClip
import os
import re
import sys

""" WARNING ! before running this script make sure you have requests,
validators and moviepy libraries installed
"""

def video_to_gif():

    url = input("Paste video url here or press Enter to use example url: ")

    if url == "":
        url = "https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55"

    if not validators.url(url):
        print(f"Your url is not valid")
        sys.exit()

    #getting video extension and something for id
    regex = re.compile(r"(com/)(.{3})(.*)(video_)([a-z0-9]*)")
    match = regex.search(url)
    v_id = match.group(2)
    ext = match.group(5)
    if ext != "mp4":
        print ("ERROR: video should be mp4")
        sys.exit()

    #downloading and saving video
    result = requests.get(url)
    video = f"tiktok_example_{v_id}.{ext}"
    print("Downloading and saving video...")
    with open(video, "wb") as f:
        f.write(result.content)
        print("Video saved in current working directory")
    v_path = os.path.join(os.getcwd(), video)

    """converting video with moviepy;
    the resulting gif is too large, so we resize video 0.5,
    set fps to 25, and it is still large :(""" 
    print("Converting video to gif. This might take a while ...")
    g_path = os.path.join(os.getcwd(), f"tiktok_example_{v_id}.gif")
    clip = VideoFileClip(v_path).resize(0.5)
    clip.write_gif(g_path, program='ffmpeg', fps=25) 
    print(f"Success. Path to your gif: {g_path}")

if __name__ == "__main__":
    video_to_gif()
