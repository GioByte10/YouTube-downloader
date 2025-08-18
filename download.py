import yt_dlp
import os

class Logger:
    @staticmethod
    def debug(msg):
        print(msg)

    @staticmethod
    def warning(msg):
        if "Unable to recognize playlist" in msg:
            msg = msg.split('.')
            print(f"\033[93m", end="")
            print(msg[0], end="")
            print(". Make sure your playlist is set to Public or Unlisted.", end="")

            if len(msg) > 1:
                print(f"{msg[1]}", end="")  # catch warnings

            print("\033[0m")

    @staticmethod
    def error(msg):
        print(msg)

os.makedirs("output", exist_ok=True)
download_format = ""

ydl_opts = {
    'ffmpeg_location': r'ffmpeg/bin',
    'ignoreerrors': True,
    'logger': Logger(),
    'retries': 10,
    'fragment_retries': 10,
}

while not download_format:
    download_format = input("\033[94mSelect download format (video, audio): \033[0m")
    download_format = download_format.strip().lower()

    if download_format == "audio":
        ydl_opts['format'] = 'bestaudio/best'
        ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]

    elif download_format == "video":
        ydl_opts['format'] = 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]'
        ydl_opts['merge_output_format'] = 'mp4'

    else:
        download_format = ""
        print("Invalid download format\n")


while True:
    inputs = input("\n\033[94mEnter YouTube URL: \033[0m")
    inputs = inputs.split()

    outtmpl = 'output/'
    video_url = inputs[0]
    no_indexing = True if (len(inputs) > 1 and inputs[1] == "--noindex") else False

    if "list=" in video_url:
        if no_indexing:
            outtmpl += r'%(playlist_title)s/%(title)s.%(ext)s'

        else:
            outtmpl += r'%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s'

    else:
        outtmpl += r'%(title)s.%(ext)s'

    ydl_opts['outtmpl'] = outtmpl

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
