from asyncio.windows_events import CONNECT_PIPE_MAX_DELAY
from pyparsing import nums
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from dataclasses import dataclass
# from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from typing import List
import requests
import time
from bs4 import BeautifulSoup


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

DRIVER_PATH = "C:\\Webdrivers\\chromedriver"
browser = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)


finalParamountMovieList = []

movieGenreUrlList = []


@dataclass
class show:
    genres: List[str]
    title: str = "NULL"
    price: str = "4.99"
    url: str = "NULL"
    ageRating: str = "NULL"
    

def getMovies():
    browser.get('https://www.paramountplus.com/movies/all/')

    while(browser.current_url != "https://www.paramountplus.com/movies/all/54" ):
        browser.execute_script("window.scrollBy(0,500)")

    time.sleep(5)

    counter = 1
    while (True):
        try:
            element = browser.find_element(By.XPATH, '/html/body/main/section[1]/div/article[' + str(counter) + ']/a/div/img')
        except NoSuchElementException:
            return
        
        title = element.get_attribute('alt')
        link = browser.find_element(By.XPATH, '/html/body/main/section[1]/div/article[' + str(counter) + ']/a')
        url = link.get_attribute('href')
        
        showData = show( genres = [])
        showData.title = str(title)
        showData.url = str(url)
        showData.genres.append("Movie")
        
        finalParamountMovieList.append(showData)
        
        counter = counter +1
        


#must come after getMovies()
def getMovieGenreURLs():
    
    counterGenres = 3
    while(True):
        try:
            genreElement = browser.find_element(By.XPATH, '/html/body/header/div[2]/ul/li['+str(counterGenres)+']/a')
        except NoSuchElementException:
            return
        
        url = genreElement.get_attribute('href')
        movieGenreUrlList.append(url)
        counterGenres = counterGenres +1
  



def appendGenreToMovie(url):
    genre = browser.current_url
    genre = genre.replace("https://www.paramountplus.com/movies/", "")
    genre = genre.replace("/","")
    genre = ''.join([i for i in genre if not i.isdigit()])
    for movie in  finalParamountMovieList:
        if(movie.url == url):
            movie.genres.append(genre)
                

def appendGenreToMoviesHelpter():
    
    counter = 1
    while(True):
        try:
            genreElement = browser.find_element(By.XPATH, '/html/body/main/section[1]/div[2]/article['+str(counter)+']/a')
        except NoSuchElementException:
            return
        
        counter = counter +1
        url = genreElement.get_attribute('href')
        appendGenreToMovie(url)
    
          
def appendGenreToMovies():
    for url in movieGenreUrlList:
        browser.get(url)
        
        oldURL = ""
        
        while(browser.current_url != oldURL ):
            oldURL = browser.current_url
            browser.execute_script("window.scrollBy(0,5000)")
            time.sleep(1)
            browser.execute_script("window.scrollBy(0,5000)")
            time.sleep(1)
            browser.execute_script("window.scrollBy(0,5000)")
            time.sleep(1)
            browser.execute_script("window.scrollBy(0,5000)")
            time.sleep(5)
            
        appendGenreToMoviesHelpter()
            
def appendAgeRating():
    for shows in finalParamountMovieList:
        time.sleep(0.1)
        
        
        r = requests.get(shows.url,  headers = headers)
        
        if (r.status_code == 200):
            soup =  BeautifulSoup( r.content, 'lxml')
            ratingElement = soup.find("span", {"class": "rating"})
            
            if(ratingElement is not None):
                shows.ageRating = ratingElement.text    

        else:
            print("error at " + shows.url)
            

getMovies()
getMovieGenreURLs()
appendGenreToMovies()

browser.close()

appendAgeRating()

file = open('ParamountMovies.txt', 'w', encoding="utf-8")

for shows in finalParamountMovieList:
    toWrite = shows.title + " { " + shows.price + " { " + shows.url + " { " + shows.ageRating;
    
    for genre in shows.genres:
        toWrite += " { " + genre
    
    file.write(toWrite + "\n")

file.close() 

