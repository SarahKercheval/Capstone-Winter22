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

allNetflixShowList = []
file = open('NetflixTitles.txt', 'w', encoding="utf-8")

for z in range(5): # max 244
    browser.get('http://ogres-crypt.com/public/NetFlix-Streaming-Genres2.html')
    genreLink = browser.find_element(By.XPATH, '/html/body/table[1]/tbody/tr[' + str(z+1) + ']/td/a')
    genreLink.click()
    time.sleep(1)
    for x in range(10): # max 15ish
        for y in range(10): # max 75ish
            try:
                title = browser.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div[2]/main/section[' + str(x+2) + ']/div/ul/li[' + str(y+1) + ']/a/span[2]')
                numID = browser.find_element(By.XPATH, '//*[@id="appMountPoint"]/div/div[2]/main/section[' + str(x+2) + ']/div/ul/li[' + str(y+1) + ']/a')
                url = numID.get_attribute('href')
                # lst = url.split('/')
                allNetflixShowList.append(title.text + " ||| " + url)
            except NoSuchElementException:
                pass

    
allNetflixShowList.sort()
# print(allNetflixShowList)

finalNetflixShowList = []
for x in allNetflixShowList:
    if x not in finalNetflixShowList:
        finalNetflixShowList.append(x)

for x in finalNetflixShowList:
    file.write(str(x) + "\n")

# print(finalNetflixShowList)

browser.close()

