

import json
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

playlist_uri = 'spotify:playlist:2e0yQbvDNb9ARfojbE4Wze'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials('f7a43754c96842d0abe4714b5d46b5b8','b220dc8a84284d15960df4b2460255ee'))



def give_data():
        playlist = spotify.playlist(playlist_uri)
        pd.json_normalize(playlist)
        playlist_items = spotify.playlist_items(playlist_uri)
        df = pd.json_normalize(playlist_items['items'])
        filter_cols = [col for col in df if col.startswith('track')]
        df = df[filter_cols]
        df.columns = [col.replace("track.","") for col in df]
        return df
