#!/usr/bin/env python3
# This is a file that contains the functions that scrapes the web to see if the lyrics are in a specified song
import requests, bs4, re

def searchLyric(specificLyric, songName, artistName):
    searchVar = "lyrics+" + artistName.replace(" ", "+")+"+"+songName.replace(" ", "+")+"+"+specificLyric.replace(" ","+")
    try:
        res = requests.get("http://www.google.com/search?q="+searchVar)
    except Exception as e:
        print("Failure to connect")
    mySoup = bs4.BeautifulSoup(res.text, "lxml")
    # element specification for results on Google
    linksFound = mySoup.select(".r a")
    if(linksFound == None):
        print("No results")
        exit(-1)
    if(scrapeGoogle(linksFound,specificLyric)>0):
        print("Lyric found in " + songName + " by " + artistName)


def scrapeGoogle(linksOnGoogle, lyric):
    # create a regex object to use to match text on page
    regexObj = re.compile(lyric, re.I)
    numSearch = min(3, len(linksOnGoogle))
    for z in range(numSearch):
        try:
            newLink = "http://www.google.com"+linksOnGoogle[z].get("href")
            print("examining link: " + newLink)
            newPage = requests.get(newLink)
            newPage.raise_for_status()
            foundMatches = regexObj.findall(newPage.text)
            if(len(foundMatches)>0):
                return 1
        except Exception as ex:
            print("Failed to get page. Continuing to next")
    return -1