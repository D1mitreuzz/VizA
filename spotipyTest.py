import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = "72da7f8b3e1b46b28833ff327b6513b7",
                                                                                                    client_secret = "f161626ec1e04578820c3553e6c5536f",
                                                                                                    redirect_uri = "http://localhost:5000",
                                                                                                    scope = "user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " - ", track['name'])