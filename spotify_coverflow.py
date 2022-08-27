import itunespy
import spotipy
import spotipy.util as util
from credentials import USERNAME, SECRET, SCOPE, URI, ID

def get_token():
    '''
    This will open a new browser window if the developer account information
    above is correct. Follow the instructions that appear in the console dialog.
    After doing this once the token will auto refresh as long as the .cache file exists
    in the root directory.
    '''

    token = util.prompt_for_user_token(USERNAME, SCOPE, ID, SECRET, URI)
    return token


def get_current_playing(token):
    '''
    Returns information about the current playing song. If no song is currently
    playing the most recent song will be returned.
    '''

    spotify = spotipy.Spotify(auth=token)
    results = spotify.current_user_playing_track()

    img_src = results["item"]["album"]["images"][0]["url"]
    artist = results["item"]["album"]["artists"][0]["name"]
    album = results["item"]["album"]["name"]
    name = results["item"]["name"]
    isrc = results["item"]["external_ids"]["isrc"]

    return {
        "img_src": img_src,
        "artist": artist,
        "album": album,
        "name": name,
        "id": isrc
    }


def itunes_search(song, artist):
    '''
    Check if iTunes has a higher definition album cover and
    return the url if found
    '''

    try:
        matches = itunespy.search_track(song)
    except LookupError:
        return None

    for match in matches:
        if match.artist_name == artist:
            return match.artwork_url_100.replace('100x100b', '5000x5000b')

def get_img(token):
    current_song = get_current_playing(token)
    hd_img = itunes_search(
        current_song["name"], current_song["artist"])

    if hd_img != None:
        return hd_img
    return current_song["img_src"]


if __name__ == "__main__":
    token = get_token()
