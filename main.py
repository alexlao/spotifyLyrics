#!/usr/bin/env python3

import lyricFinder, playlistSearch
targetLyric = input("Input lyric you are looking for: ")
targetURI = input("Input SPOTIFY URI of PLAYLIST it may be in: ")
# playlist = playlistSearch.unwrapPlaylist("spotify:user:theninjanaren:playlist:1gU2CHLlcpVDxpaDRAmJOr")
playlist = playlistSearch.unwrapPlaylist(targetURI)
for o in range(len(playlist["items"])):
    lyricFinder.searchLyric(targetLyric,playlist["items"][o]["track"]["name"],playlist["items"][o]["track"]["artists"][0]["name"])