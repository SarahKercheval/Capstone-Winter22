import requests
import time
from bs4 import BeautifulSoup

#HBO max provides a more in depth sitemap to chrome users
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}

r = requests.get("https://www.hbomax.com/static/sitemap.xml", headers = headers)
soup = BeautifulSoup( r.content, 'lxml')

r = requests.post(url="https://www.hbomax.com/static/sitemap.xml", headers={'Connection':'close'})

linksConglomerated = soup.getText("@@@@@", strip = True)
links = linksConglomerated.split("@@@@@")

file = open('HBOTitles.txt', 'w', encoding="utf-8")
file2 = open('HBOErrors.txt', 'w', encoding="utf-8")


length = len(links)

for i in range(length):
    
    r = requests.get(links[i], headers = headers)
    
    if (r.status_code == 200):
    
        soup = BeautifulSoup( r.content, 'lxml')
        
        r = requests.post(links[i], headers={'Connection':'close'})
        
        linksConglomerated = soup.getText("@@@@@", strip = True)
        links2 = linksConglomerated.split("@@@@@")
        
        validateLink1 = links2[0].split("series")
        validateLink2 = links2[0].split("feature")
        
        if (len(validateLink1) > 1 or len(validateLink2) > 1):
            r = requests.get(links2[0], headers = headers)
            soup = BeautifulSoup(r.content, "html.parser")
            
            if(r.status_code == 200):
                if(soup.find('title') is not None):
                    title = soup.find('title').text
                    title = title.replace("(HBO) - Stream TV Shows | HBO Max", "")
                    title = title.replace(" | HBO Original", "")
                    title = title.replace(" - Stream Movies", "")
                    title = title.replace(" - Stream TV Shows", "")
                    title = title.replace(" | Now Streaming |  HBO Max Originals", "")
                    title = title.replace(" | Start Streaming Today", "")
                    title = title.replace(" | HBO Max Originals", "")
                    title = title.replace(" | HBO Max", "")
                    title = title.replace(" (HBO)", "")
                    titleTokens = title.split(" ")
                    
                    if(titleTokens[0] == "Watch"):
                        title = title[6:]
                        
                    file.write(title + " ||| " + links2[0] + "\n")
                else:
                    file2.write(links2[0] + "\n")
                    file2.flush()
                    
                    #need to get rid of leading watch
            elif(r.status_code == 404):
                pass
            else:
                file2.write("status code " + str(r.status_code) +" at " + links2[0] + "\n")
            
    elif (r.status_code == 404):
        pass
    else:
        file2.write("status code " + str(r.status_code) +" at " + links[i] + "\n")
                
    time.sleep(0.1)
    
file.close()
file2.close()




