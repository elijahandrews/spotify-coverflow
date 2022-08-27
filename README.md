# SpotifyCoverFlow

My fork of http://github.com/kylesurowiec/spotify-coverflow, thanks for the great
starting point!

Spotify is great, but has a few problems with the way it treats album art:
1. it's difficult (if not impossible) to see album art for your currently playing track in full screen
2. the artwork is pretty low resolution (600x600)

This program serves high resolution artwork for your currently playing spotify
song via http. It reaches out to iTunes to find higher resolution artwork, and
serves that if available.

The idea is that you run this server somewhere on your local
network, and then access the artwork from any laptop/tablet/phone. I use this to
see nice artwork on my iPad when I'm sitting on the couch listening to music.

Keys and callback URI are given with your personal Spotify developer account, register here: [Spotify Developer](https://developer.spotify.com/my-applications/#!/). They go in credentials.py
