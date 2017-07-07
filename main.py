#!/usr/bin/env python3

import lyricFinder, playlistSearch

# lyricFinder.searchLyric("lick it up", "ice cream truck", "cazwell")
# playlistSearch.getUser("spotify:user:theninjanaren:playlist:1gU2CHLlcpVDxpaDRAmJOr")
playlist = playlistSearch.unwrapPlaylist("spotify:user:theninjanaren:playlist:1gU2CHLlcpVDxpaDRAmJOr")
for o in range(len(playlist["items"])):
    lyricFinder.searchLyric("lick it up", playlist["items"][o]["track"]["artists"][0]["name"],playlist["items"][o]["track"]["name"])