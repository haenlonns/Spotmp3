# Samuel Bai
# 01/14/2023
# Downloads all URLs in a txt file into mp3 files

from __future__ import unicode_literals
from yt_dlp import YoutubeDL


# Samuel Bai
# 01/14/2023
# downloadURL(name, urlString) downloads a mp3 file with name [name].mp3 given
#   YT URL urlstring
def downloadURL(name, urlString):

    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio' : True,
        'outtmpl': f'{name}.mp3',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([urlString])


# Samuel Bai
# 01/14/2023
# downloadPlaylist(nameFile, urlFile) downloads all URLs in urlfile as mp3 files
#   with file names as [name].mp3
def downloadPlaylist(nameFile, urlFile):
    
    with open(urlFile, 'r', encoding='utf-8') as urls, open(nameFile, 'r', encoding='utf-8') as names:
        
        songURLs = urls.read().splitlines()
        songNames = names.read().splitlines()

        for i in range(len(songNames)):
            downloadURL(songNames[i], songURLs[i])
