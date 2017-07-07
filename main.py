#!/usr/bin/env python3

import lyricFinder, playlistSearch

playlist = playlistSearch.unwrapPlaylist("spotify:user:theninjanaren:playlist:1gU2CHLlcpVDxpaDRAmJOr")
for o in range(len(playlist["items"])):
    lyricFinder.searchLyric("lick it up",playlist["items"][o]["track"]["name"],playlist["items"][o]["track"]["artists"][0]["name"])