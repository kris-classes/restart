import dotify
from fastapi import FastAPI

app = FastAPI()

# API Endpoints:
#   /playlists = returns list of playlists
#   /playlists/{id} = returns playlist id
#


@app.get("/")
def welcome():
    return "<b>Welcome to Dotify!</b>"


@app.get("/playlists")
def playlists():
    return dotify.playlists


@app.get("/playlists/{playlist_id}")
def playlist_by_id(playlist_id):
    playlist_id = int(playlist_id)
    playlist_length = len(dotify.playlists)
    if playlist_id > playlist_length or playlist_id < 0:
        return "Invalid Playlist ID"
    else:
        return dotify.playlists[playlist_id]
