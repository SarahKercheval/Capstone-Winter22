from dataclasses import dataclass
from bs4 import BeautifulSoup
from typing import List
import requests
import time


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

finalParamountShowList = []

showGenreUrlList = []


@dataclass
class show:
    genres: List[str]
    title: str = "NULL"
    price: str = "4.99"
    url: str = "NULL"
    ageRating: str = "NULL"



def getGenreUrlList(soup):
    urlHeader = soup.find("ul", {"class": "subnav__items"})
    urlElements = urlHeader.find_all('a')
    
    for element in range(3, len(urlElements)):
        url = "https://www.paramountplus.com" + urlElements[element].get('href')
        showGenreUrlList.append(url)

def getShows():
    
    r = requests.get("https://www.paramountplus.com/shows/all/", headers = headers)
    
    if(r.status_code == 200):
        soup =  BeautifulSoup( r.content, 'lxml')
        showInfo = soup.find_all("article", {"class": "show-browse-item"})
        
        for data in showInfo:
            text = str(data)
            
            url = text[text.find("href"):text.find("/\">")]
            url = url[7:]
            url = "https://www.paramountplus.com/" + url
            
            title = text[text.find("<img alt=\""):text.find("\" class")]
            title = title[10:]
            
            showElement = show(title = title, url = url, genres = ["show"])
            finalParamountShowList .append(showElement)
          
        getGenreUrlList(soup)
        
    else:
        print("status code: " + r.status_code)
    

def appendShowGenres():
    for genreUrl in showGenreUrlList:
        r = requests.get(genreUrl, headers = headers)
        
        if(r.status_code == 200):
            
            genre = genreUrl.replace("https://www.paramountplus.com/shows/","")
            genre = genre[:(len(genre) -1)]
            
            soup = BeautifulSoup( r.content, 'lxml')
            
            allGenreElementHeader = soup.find_all("div", {"class": "show-browse-grid grid portrait"})
            
            if(len(allGenreElementHeader) == 2):
                genreElementHeader = allGenreElementHeader[1]
            else:
                genreElementHeader = allGenreElementHeader[0]
            
            
            elementList = genreElementHeader.find_all('a')
            
            for element in elementList:
                url = "https://www.paramountplus.com" + element.get('href')
                
                if(url[len(url) -1] == "/"):
                    url = url[:(len(url) -1)]
                
            
                for theShow in finalParamountShowList:
                               
                    if(theShow.url == url):
                        theShow.genres.append(genre)
            
            
            
            
            
            
            
        else:
            print("status code: " + r.status_code)



def appendAgeRating():
    for shows in finalParamountShowList:
        time.sleep(0.1)
        
        
        r = requests.get(shows.url,  headers = headers)
        
        if (r.status_code == 200):
            soup =  BeautifulSoup( r.content, 'lxml')
            ratingElement = soup.find("span", {"class": "rating"})
            
            if(ratingElement is not None):
                shows.ageRating = ratingElement.text    

        else:
            print("error at " + shows.url)




##next add age ratings
#some shows are broken



getShows()
appendShowGenres()
appendAgeRating()


file = open('ParamountShows.txt', 'w', encoding="utf-8")

for shows in finalParamountShowList:
    toWrite = shows.title + " { " + shows.price + " { " + shows.url + " { " + shows.ageRating;
    
    for genre in shows.genres:
        toWrite += " { " + genre
    
    file.write(toWrite + "\n")

file.close() 