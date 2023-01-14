import spotipy
from spotipy.oauth2 import SpotifyOAuth

sparkler = open("sparkler.txt", 'w', encoding='utf-8')

def show_tracks(results):
    for i, item in enumerate(results['items']):
        track = item['track']
        sparkler.write(f"{track['name']} by {track['artists'][0]['name']} Lyric Video \n")


if __name__ == '__main__':
    scope = 'playlist-read-private'
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    playlists = sp.current_user_playlists()
    user_id = sp.me()['id']
    results = sp.playlist(playlist_id="0x1JvPaVtrGTiv8Kmx6FGK", fields="tracks,next")
    tracks = results['tracks']
    show_tracks(tracks)

"""
for playlist in playlists['items']:
        if playlist['owner']['id'] == user_id:
            print()
            print(playlist['name'])
            print('  total tracks', playlist['tracks']['total'])

            results = sp.playlist(playlist['id'], fields="tracks,next")
            tracks = results['tracks']
            show_tracks(tracks)

            while tracks['next']:
                tracks = sp.next(tracks)
                show_tracks(tracks)
"""
    


