import requests
import time
from bs4 import BeautifulSoup
from typing import List
from dataclasses import dataclass


@dataclass
class show:
    genres: List[str]
    title: str = "NULL"
    price: str = "6.99"
    url: str = "NULL"
    ageRating: str = "NULL"



allHuluShowList = []
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

def getShowData():
    r = requests.get("https://www.hulu.com/sitemap/series", headers = headers)
    soup1 = BeautifulSoup( r.content, 'lxml')
    titles1 = soup1.find_all("div", {"class": "ListCardItem__item"})

    for title in titles1:
        url =  title.a['href']
        url = url.replace("?lp_referrer=sitemappage", "")
        url = "https://www.hulu.com" + url 
        
        theShow = show(title = title.text, url = url, genres = ["show"])
        
        allHuluShowList.append(theShow)
        
def getMovieData():
    r = requests.get("https://www.hulu.com/sitemap/movies", headers = headers)
    soup1 = BeautifulSoup( r.content, 'lxml')
    titles1 = soup1.find_all("div", {"class": "ListCardItem__item"})

    for title in titles1:
        url =  title.a['href']
        url = url.replace("?lp_referrer=sitemappage", "")
        url = "https://www.hulu.com" + url 
        
        theShow = show(title = title.text, url = url, genres = ["movie"])
        
        allHuluShowList.append(theShow)        
        

def getRatingAndGenres():
    for theShow in allHuluShowList:
        time.sleep(0.1)
        r = requests.get(theShow.url, headers = headers)
        
        if(r.status_code == 200):
            
            if(len(r.history) == 0):
                    
                soup = BeautifulSoup( r.content, 'lxml')
                rating = soup.find("span", {"class": "DetailEntityMetadata__rating"})         
                genreHeader = soup.find("span", {"class": "DetailEntityMetadata__genres"})
                       
                if(rating is not None):
                    theShow.ageRating = rating.text
                    
                if(genreHeader is not None):
                    genreList = genreHeader.find_all('a')
                    
                    if (genreList == []):
                        genreList = genreHeader.find_all('span')
                    
                    for genre in genreList:
                        theShow.genres.append(genre.text)
                        
            else:
                theShow.price = "13.99"
                    
        else:
            print(str(r.status_code) + " " + theShow.title)
        
        
        
getShowData()       
getMovieData()      
getRatingAndGenres()

file = open('HuluShows.txt', 'w', encoding="utf-8")

for shows in allHuluShowList:
    toWrite = shows.title + " { " + shows.price + " { " + shows.url + " { " + shows.ageRating;
    
    for genre in shows.genres:
        toWrite += " { " + genre
    
    file.write(toWrite + "\n")

file.close()       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
