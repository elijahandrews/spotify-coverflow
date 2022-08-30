import coverpy
import deezer
import itunespy
import spotipy
import spotipy.util as util
import requests
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
    if results is None:
        return None

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


def itunes_search(song, artist, album):
    '''
    Check if other sources have higher definition album covers and
    return the url if found
    '''


    # try itunespy with track
    matches = None
    try:
        matches = itunespy.search_track(song)
    except LookupError:
        pass
    if matches:
        # direct match on album
        for match in matches:
            if match.artist_name == artist and match.collectionName == album:
                return match.artwork_url_100.replace('100x100b', '10000x10000b')

        # fuzzy match on album
        for match in matches:
            if match.artist_name == artist and match.collectionName.startswith(album):
                return match.artwork_url_100.replace('100x100b', '10000x10000b')

    # try coverpy with album + artist
    c = coverpy.CoverPy()
    try:
        query = album + " " + artist
        result = c.get_cover(query, 10)
        # return result.artwork(10000)
    except (coverpy.exceptions.NoResultsException, requests.exceptions.HTTPError):
        pass

    # deezer
    client = deezer.Client()
    res = client.search(track=song, artist=artist, album=album)
    if len(res) > 0:
        return res[0].album.cover_xl

    return None



def get_img(token):
    current_song = get_current_playing(token)
    if current_song is None:
        return None
    hd_img = itunes_search(
        current_song["name"], current_song["artist"], current_song["album"])

    if hd_img != None:
        return hd_img
    return current_song["img_src"]


if __name__ == "__main__":
    token = get_token()
