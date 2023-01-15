# Samuel Bai
# 01/14/2023
# Places song name and artist in a spotify playlist into a txt file
#   given the playlist id

import spotipy
from spotipy.oauth2 import SpotifyOAuth


# Samuel Bai
# 01/14/2023
# strRename(oldStr) replaces illegal file name chars in oldStr with legal ones
def strRename(oldStr):
    
    newStr = oldStr.replace('<', '(') \
                .replace('>', ')') \
                .replace('/', ' ') \
                .replace('\\', ' ') \
                .replace('|', '-') \
                .replace(':', '-') \
                .replace('?', ' ') \
                .replace('"', "''") \
                .replace('*', "''")
    
    return newStr


# Samuel Bai
# 01/14/2023
# getTrackName(item) produces the track title and artist as a str
#   given an item from spotipy
def getTrackName(item):
    
    track = item['track']
    songEntry = f"{track['name']} by {track['artists'][0]['name']}\n"
    fixedSongEntry = strRename(songEntry)
    
    return fixedSongEntry


# Samuel Bai
# 01/14/2023
# sendPlaylisttoTxt(results) writes a txt file with each line ocntaining
#   the track title followed by the artist name
def sendPlaylisttoTxt(results):

    playlistName = results['name']
    tracks = results['tracks']
    
    with open(f"{playlistName}.txt", 'a', encoding='utf-8') as playlistFile:
        for item in tracks['items']:
            track = getTrackName(item)
            playlistFile.write(track)
