import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials

#scopeID = "user-library-read"# Первый вариант использования Scope с прочтением любимых треков
scopeID = "user-read-currently-playing"
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = "72da7f8b3e1b46b28833ff327b6513b7",
                                                                                                    client_secret = "f161626ec1e04578820c3553e6c5536f",
                                                                                                    redirect_uri = "http://localhost:5000",
                                                                                                    scope = scopeID))

"""results = sp.current_user_saved_tracks()
print(results)
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])"""# №1

#spotify = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials())
result = sp.current_user_playing_track()
print(result)
