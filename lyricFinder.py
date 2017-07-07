#!/usr/bin/env python3
# This is a file that contains the functions that scrapes the web to see if the lyrics are in a specified song
import requests, bs4, re

# given a specific lyric, songName, and artistName, it will search google for it.
# Links found on google is passed to scrapeGoogle(). If lyric found, it will print song information.
def searchLyric(specificLyric, songName, artistName):
    # searchVar = "lyrics+" + artistName.replace(" ", "+")+"+"+songName.replace(" ", "+")+"+"+specificLyric.replace(" ","+")
    searchVar = "lyrics+" + artistName.replace(" ", "+")+"+"+songName.replace(" ", "+")
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
        print("#####LYRIC FOUND#####"+" \n Lyric found in " + songName + " by " + artistName + "\n#####################")

# scrapes pages for matching lyrics. If match found, returns 1. Otherwise, returns -1
def scrapeGoogle(linksOnGoogle, lyric):
    # create a regex object to use to match text on page
    regexObj = re.compile(lyric, re.I)
    numSearch = min(3, len(linksOnGoogle))
    for z in range(numSearch):
        try:
            newLink = "http://www.google.com"+linksOnGoogle[z].get("href")
            # print("examining link: " + newLink)
            newPage = requests.get(newLink)
            newPage.raise_for_status()
            foundMatches = regexObj.findall(newPage.text)
            if(len(foundMatches)>0):
                print(newLink)
                return 1
        except Exception as ex:
            # print("Failed to get page. Continuing to next")
            pass
    return -1