# Samuel Bai
# 01/14/2022
# Takes in a Spotify Playlist URL and downloads mp3 files of all songs

import os

import spotipy
from spotipy.oauth2 import SpotifyOAuth

import playlistPull
import playlistConvert
import downloadURLs


# Samuel Bai
# 01/14/2022
# playlisttomp3(url) downloads all songs from a spotify playlist url
# and places it into a directory with its name being playlist name
def playlisttomp3(url):
    
    id = url[34:56]

    scope = 'playlist-read-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    results = sp.playlist(playlist_id=id, fields="tracks,next,name")
    fileName = playlistPull.strRename(results['name']).strip()

    downloadPath = os.path.join(os.path.expanduser('~'), f'downloads\{fileName}')

    if not os.path.exists(downloadPath):
        os.mkdir(downloadPath)
    
    os.chdir(downloadPath)
    
    playlistPull.sendPlaylisttoTxt(results)
    playlistConvert.genPlaylistURLs(f'{fileName}.txt', f'{fileName}URLs.txt')
    downloadURLs.downloadPlaylist(f'{fileName}.txt', f'{fileName}URLs.txt')

    os.remove(f'{downloadPath}/{fileName}.txt')
    os.remove(f'{downloadPath}/{fileName}URLs.txt')


if __name__ == "__main__":
    url = input("Enter URL: ")
    playlisttomp3(url)
