# Samuel Bai
# 01/14/2023
# Converts all the songs in a given txt file to URLs

from youtubesearchpython import VideosSearch


# Samuel Bai
# 01/14/2023
# convertNameURL(searchStr) finds the URL of first YT 
#   search result of searchStr
def convertNameURL(searchStr):
    
    result = VideosSearch(searchStr, limit=1).result()
    URL = result['result'][0]['link']

    return URL


# Samuel Bai
# 01/14/2023
# genPlaylistURLs(txtIn, txtOut) searches all song titles in txtIn and
#   returns their YT URLs in txtOut
def genPlaylistURLs(txtIn, txtOut):

    resultURLs = open(txtOut, 'a')

    with open(txtIn, 'r', encoding='utf-8') as songSearches:
        for songSearch in songSearches:
            songURL = convertNameURL(f"{songSearch} Lyric Video")
            resultURLs.write(f"{songURL}\n")
