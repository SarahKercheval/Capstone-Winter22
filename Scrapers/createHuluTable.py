import requests
import time
from bs4 import BeautifulSoup

file = open('HuluTitles.txt', 'w', encoding="utf-8")

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

allHuluShowList = []

r1 = requests.get("https://www.hulu.com/sitemap/series", headers = headers)
r2 = requests.get("https://www.hulu.com/sitemap/movies", headers = headers)

soup1 = BeautifulSoup( r1.content, 'lxml')
soup2 = BeautifulSoup( r2.content, 'lxml')

r1 = requests.post(url="https://www.hulu.com/sitemap/series", headers={'Connection':'close'})
r2 = requests.post(url="https://www.hulu.com/sitemap/movies", headers={'Connection':'close'})

titles1 = soup1.find_all("div", {"class": "ListCardItem__item"})
titles2 = soup2.find_all("div", {"class": "ListCardItem__item"})

for title in titles1:
    url =  title.a['href']
    url = url.replace("?lp_referrer=sitemappage", "")
    url = "https://www.hulu.com" + url 
    allHuluShowList.append(title.text + " ||| " + url)

for title in titles2:
    url =  title.a['href']
    url = url.replace("?lp_referrer=sitemappage", "")
    url = "https://www.hulu.com" + url 
    allHuluShowList.append(title.text + " ||| " + url)


allHuluShowList.sort()

for e in allHuluShowList:
    file.write(e + "\n")
    
file.close()