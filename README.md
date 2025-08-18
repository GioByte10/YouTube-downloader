# YouTube-downloader
This media converter tool allows you to download YouTube videos into `.mp4` files and/or extract their audio and download as `.mp3` files. Although this tool is mainly used to download YouTube files, since it uses the [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) library you should also be able to download from other sites such as Vimeo, Facebook, Instagram, Reddit, SoundCloud, Twitter / X, TikTok, Twitch, amongst hundreds of other websites listed [here](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md)

## Usage
First select the download format you want. All of your files will be downloaded in the `YTD_output` folder
<br>
<br>
<img width="736" height="149" alt="image" src="https://github.com/user-attachments/assets/1592028a-a71c-4810-84b6-87d38b351bac" />
<br>
<br>

For a single file download enter the YouTube link, e.g., `Alright` from Kendrick Lamar
```
https://www.youtube.com/watch?v=JocAXINz-YE
```
<img width="888" height="720" alt="image" src="https://github.com/user-attachments/assets/b2ab2fa6-d5be-48ef-9664-82e0abc34021" />
<br>
<br>

To download an entire playlist either enter the playlist share link, e.g.,
```
https://youtube.com/playlist?list=PLTbIck9Ffg_Zij47uTleuMzCGtwq_Ia7X
```
<img width="823" height="693" alt="image" src="https://github.com/user-attachments/assets/ea62e461-55d0-4484-a441-44e73e9d1102" />
<br>
<br>

or the link of any song obtained through the playlist
```
https://www.youtube.com/watch?v=JocAXINz-YE&list=PLTbIck9Ffg_Zij47uTleuMzCGtwq_Ia7X
```
<img width="887" height="956" alt="image" src="https://github.com/user-attachments/assets/a6ba14e1-9b82-4d2b-afc3-bf2878c6c25c" />
<br>
<br>

By default your playlist files will be indexed in the order they appear on the playlist, e.g., 
<img width="783" height="179" alt="image" src="https://github.com/user-attachments/assets/2dea3a7c-215a-492c-8cf9-1ac53db8ce71" />
<br>
<br>

If you do not want your files indexed, make sure to add the `--noindex` argument when inputting the YouTube URL, e.g.,
```
https://www.youtube.com/watch?v=JocAXINz-YE&list=PLTbIck9Ffg_Zij47uTleuMzCGtwq_Ia7X --noindex
```
<img width="785" height="195" alt="image" src="https://github.com/user-attachments/assets/0bafe97d-6af4-455a-9ec2-7395e386432d" />
<br>
<br>



_Note that your playlist privacy must be set to `Public` or `Unlisted` for the program to be able to access it_
<br>

# Running the program
There are two ways to run the program, either using the standalone Windows executable or through Python

## Executable
Run `download.exe`

## Python
Make sure you have Python >= 3.9. You can check your python version by running
```
python --version
```

Install the yt-dlp library
```
pip install yt-dlp
```

On the terminal, cd into the `YouTube-downloader` folder
```
cd path\to\YouTube-downloader
```

Run `download.py`
```
python download.py
```

## File Transfering
If you are planning on sharing these files across devices, I recommend checking out [LocalSend](https://localsend.org), a "free, open-source app that allows you to securely share files and messages with nearby devices over your local network without needing an internet connection."

