from pyparsing import nums
from selenium import webdriver
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
# from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

site = "https://www.netflix.com/"

show = input("What would you like to find?")
search = show.replace(" ","")


DRIVER_PATH = "C:\\Webdrivers\\chromedriver"
browser = webdriver.Chrome(executable_path=DRIVER_PATH)
browser.get(site + search)

try:
    unavaliable = browser.find_element(By.XPATH,'//*[@id="appMountPoint"]/div/div/div[2]/h1')
except NoSuchElementException:
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
    browser.close()
else:
    print("Show not found")
    browser.close()