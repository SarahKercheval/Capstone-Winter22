import requests
from typing import List
from dataclasses import dataclass
from bs4 import BeautifulSoup
import time
import os

@dataclass
class show:
    genres: List[str]
    title: str = "NULL"
    price: str = "NULL"
    url: str = "NULL"
    ageRating: str = "NULL"


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

r = requests.get("http://ogres-crypt.com/public/NetFlix-Streaming-Genres2.html", headers = headers)

netflixShows = []
netflixShowsTextList = []
showInList = False
ratingText = "NULL"
counter = 0
counter2 = 0

if(r.status_code == 200):
    soup = BeautifulSoup( r.content, 'lxml')
    genreInfo = soup.find_all('a')
    
    for genre in genreInfo:
        
        counter2 = counter2 + 1
        
        time.sleep(0.1)
        
        genreName = genre.text
        genreName = genreName[:genreName.find("(") -1]
        
        genreUrl = genre.get('href')
    
        r2 = requests.get(genreUrl , headers = headers)
        
        if(r2.status_code == 200):
            
            soup2 = BeautifulSoup( r2.content, 'lxml')
            shows = soup2.find_all('a', {"class": "nm-collections-title nm-collections-link"})
            
            
            for theShow in shows:
                
                counter = counter +1
                
                showTitle = theShow.text
                showUrl = theShow.get('href')
                
                for element in netflixShows:
                    if(element.url == showUrl):
                        element.genres.append(genreName)
                        showInList = True
                if(not showInList):
                    time.sleep(0.1)
                    r3 = requests.get(showUrl, headers = headers)
                    
                    if (r3.status_code == 200):
                        soup3 = BeautifulSoup( r3.content, 'lxml')
                        rating = soup3.find("span", {"class": "maturity-number"})
                        
                        if (rating is not None):
                            ratingText = rating.text
                    else:
                        print("1 " + r3.status_code)
                    newShow = show(title = showTitle, url = showUrl, ageRating = ratingText, genres = [genreName])
                    netflixShows.append(newShow)
                    
                showInList = False
                ratingText = "NULL"
      

    for e in netflixShows:
        toWrite = e.title + " { " + e.price + " { " + e.url + " { " + e.ageRating
    
        for genre in e.genres:
            toWrite += " { " + genre
            
        netflixShowsTextList.append(toWrite)
        
    netflixShowsTextList.sort()
    
    file = open('NetflixShows.txt', 'w', encoding="utf-8")
    
    for el in netflixShowsTextList:
        file.write(el + "\n")
    
    file.close()
    
    
    file = open("NetflixShows.txt", "r", encoding="utf-8")
    
    fileLines = []
    
    
    for x in file:
        line = x
        elements = line.split("{")
        
        elements[-1] = elements[-1].replace("\n", " ")
        
        duplicatesRemoved = []
    
        a = set()
        for e in elements:
            if e not in a:
                a.add(e)
                duplicatesRemoved.append(e)
        
        
        toAdd = ""
        first = True
        for el in duplicatesRemoved:
            if first:
                toAdd += el
                first = False
            else:
                toAdd += "{" + el
                
        fileLines.append(toAdd)
        
        
    file.close()
    os.remove("newfile.txt")

    file2 = open("newfile.txt", "w", encoding="utf-8")
    
    for e in fileLines:
        file2.write(e + "\n")
        
    file2.close()
    
else:
    print(r.status_code)