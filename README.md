# YouTube-downloader
This media converter tool allows you to download YouTube videos into `.mp4` files and/or extract their audio and download as `.mp3` files

## Usage
For a single file download enter the YouTube link, e.g., `Alright` from Kendric Lamar
```
https://www.youtube.com/watch?v=JocAXINz-YE
```
<img width="888" height="720" alt="image" src="https://github.com/user-attachments/assets/b2ab2fa6-d5be-48ef-9664-82e0abc34021" />
<br>
<br>
<br>

To download an entire playlist either enter the playlist share link, e.g.,
```
https://youtube.com/playlist?list=PLTbIck9Ffg_Zij47uTleuMzCGtwq_Ia7X
```
<img width="823" height="693" alt="image" src="https://github.com/user-attachments/assets/ea62e461-55d0-4484-a441-44e73e9d1102" />
<br>
<br>
<br>


or the link of any song obtained through the playlist
```
https://www.youtube.com/watch?v=JocAXINz-YE&list=PLTbIck9Ffg_Zij47uTleuMzCGtwq_Ia7X
```
<img width="887" height="956" alt="image" src="https://github.com/user-attachments/assets/a6ba14e1-9b82-4d2b-afc3-bf2878c6c25c" />
<br>
<br>
<br>



## Apendix on query parameters
To better understand how to this tool works we must first understand how URLs' query parameters work. A query parameter assigns values to specified parameters, in other words, it provides extra information to the website we are accessing. They do it in the following format: `URL?parameter=value`. In the case of YouTube, the most important parameter is the video ID, which tells YouTube exactly which video you are watching. This parameter is denoted by `v`. Let's look at an example of a YouTube music video, `Alright`, from Kendric Lamar
```diff
https://www.youtube.com/watch?v=JocAXINz-YE
```
Here we see the query
```
?v=JocAXINz-YE
```
which contains the `JocAXINz-YE` video ID
