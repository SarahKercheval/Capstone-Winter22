from pyparsing import nums
from selenium import webdriver
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
# from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By



netflix = "netflix"
hulu = "hulu"

site = input("What site would you like to search?")

siteURL = "https://www." + site + ".com/"

show = input("What would you like to find?")
search = " ".join(show.split())

def scrapeNetflix(siteURL):

    DRIVER_PATH = "C:\\Webdrivers\\chromedriver"
    browser = webdriver.Chrome(executable_path=DRIVER_PATH)
    browser.get(siteURL + search)

    try:
        unavaliable = browser.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div[2]/h1')
    except NoSuchElementException:
        
        try:
            print("Show was found")
            yearReleased = browser.find_element(By.XPATH,'//*[@id="section-hero"]/div[1]/div[1]/div[2]/div/div[1]/span[1]')
            maturityRating = browser.find_element(By.XPATH,'//*[@id="section-hero"]/div[1]/div[1]/div[2]/div/div[1]/span[3]/span/span')
            numSeasons = browser.find_element(By.XPATH,'//*[@id="section-hero"]/div[1]/div[1]/div[2]/div/div[1]/span[5]/span/span')
            genre = browser.find_element(By.XPATH,'//*[@id="section-hero"]/div[1]/div[1]/div[2]/div/div[1]/a')
            synopsis = browser.find_element(By.XPATH,'//*[@id="section-hero"]/div[1]/div[1]/div[2]/div/div[2]/div')
            print(yearReleased.text)
            print(maturityRating.text)
            print(numSeasons.text)
            print(genre.text)
            print(synopsis.text)
            # browser.close()
        except NoSuchElementException:
            print("multiple shows match criteria")
            elementlist =  browser.find_elements(By.CLASS_NAME, 'nm-collections-title nm-collections-link')
            print(elementlist)
            
            #browser.get(netflix + ".com/title/" + )
            
            
            
            
            
            
                
    else:
        print("Show not found")
        # browser.close()

def scrapeHulu(siteURL):

    find = search.replace(" ","-")
    DRIVER_PATH = "C:\\Webdrivers\\chromedriver"
    browser = webdriver.Chrome(executable_path=DRIVER_PATH)
    browser.get(siteURL + find)

    try:
        unavaliable = browser.find_element(By.XPATH,'//*[@id="__next"]/div/p[2]')
    except NoSuchElementException:
        print("Show was found")
        yearReleased = browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/span[4]')
        maturityRating = browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/span[1]')
        numSeasons = browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[1]/div[2]/div[1]/div[1]/div[1]')
        genre = browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div/span[2]')
        synopsis = browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/div/div[1]/div[2]/div[1]/div[1]/p[1]/span[1]')
        print(yearReleased.text)
        print(maturityRating.text)
        print(numSeasons.text)
        print(genre.text)
        print(synopsis.text)
    else:
        print("Show not found")
    

if netflix in siteURL:
    scrapeNetflix(siteURL)
elif hulu in siteURL:
    scrapeHulu(siteURL)
else:
   print("Site not recongized")






