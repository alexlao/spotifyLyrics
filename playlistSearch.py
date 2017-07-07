from spotipy.oauth2 import SpotifyClientCredentials
import requests, json, pprint, spotipy

def unwrapPlaylist(uri):
    client_login = SpotifyClientCredentials(client_id="b70925da32af4ab0a23d11bb88254e56",client_secret="80581a8245a34f808d5efdd7b9e171ab")
    sp = spotipy.Spotify(client_credentials_manager = client_login)
    user = getUser(uri)
    playlistTracks = sp.user_playlist_tracks(user, uri)
    return playlistTracks

def getUser(uri):
    tokens = uri.split(":")
    # print(tokens[2])
    return tokens[2]