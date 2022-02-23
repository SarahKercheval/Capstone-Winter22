from asyncio.windows_events import CONNECT_PIPE_MAX_DELAY
from pyparsing import nums
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
# from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

DRIVER_PATH = "C:\\Webdrivers\\chromedriver"
browser = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)

finalParamountMovieList = []
finalParamountShowList = []

showList = []


browser.get('https://www.paramountplus.com/movies/all/')

while(browser.current_url != "https://www.paramountplus.com/movies/all/54" ):
    browser.execute_script("window.scrollBy(0,500)")

time.sleep(5)

counter = 1
while (True):
    try:
        name = browser.find_element(By.XPATH, '/html/body/main/section[1]/div/article[' + str(counter) + ']/a/div/img')
        counter = counter + 1
    except:
        counter = counter -1
        break

for x in range(1, counter): # max 2267
    try:
        name = browser.find_element(By.XPATH, '/html/body/main/section[1]/div/article[' + str(x) + ']/a/div/img')
        title = name.get_attribute('alt')
        link = browser.find_element(By.XPATH, '/html/body/main/section[1]/div/article[' + str(x) + ']/a')
        url = link.get_attribute('href')
        finalParamountMovieList.append(title + " ||| " + url)
    except NoSuchElementException:
        print("error ar " + str(x))



for x in finalParamountMovieList:
    showList.append(x)


browser.get('https://www.paramountplus.com/shows/all/')
time.sleep(5)




counterX = 1
indexLimitY = []
while (True):
    try:
        name = browser.find_element(By.XPATH, '/html/body/main/section[1]/div[' + str(counterX) + ']/article[1]/a/div/img')
        counterX = counterX +1
    except:
        break
    
counterY = 1
for x in range(1, counterX):
    while (True):
        try:
            name = browser.find_element(By.XPATH, '/html/body/main/section[1]/div[' + str(x) + ']/article['+ str(counterY) +']/a/div/img')
            counterY = counterY +1
        except:
            indexLimitY.append(counterY)
            counterY = 1
            break
        








for x in range(1, counterX): # max 27
    for y in range(1, indexLimitY[x-1]): # max 70?
        try:
            name = browser.find_element(By.XPATH, '/html/body/main/section[1]/div[' + str(x) + ']/article[' + str(y) + ']/a/div/img')
            title = name.get_attribute('alt')
            link = browser.find_element(By.XPATH, '/html/body/main/section[1]/div[' + str(x) + ']/article[' + str(y) + ']/a')
            url = link.get_attribute('href')
            finalParamountShowList.append(str(title) + " ||| " + str(url))
        except NoSuchElementException:
            break


for x in finalParamountShowList:
    showList.append(x)
    
showList.sort()

file = open('ParamountTitles.txt', 'w', encoding="utf-8")

for element in showList:
    file.write(element + "\n")
    
file.close()

browser.close()