from selenium import webdriver
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
# from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

DRIVER_PATH = "C:\\Webdrivers\\chromedriver"
browser = webdriver.Chrome(executable_path=DRIVER_PATH)
browser.get("https://www.imdb.com/search/title/")


Action =  browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[1]/td[1]/label")
Adventure = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[1]/td[2]/label")
Animation = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[1]/td[3]/label")
Biography = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[1]/td[4]/label")

Comedy = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[2]/td[1]/label")
Crime = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[2]/td[2]/label")
Documentary = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[2]/td[3]/label")
Drama = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[2]/td[4]/label")

Family = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[3]/td[1]/label")
Fantasy = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[3]/td[2]/label")
FilmNoir = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[3]/td[3]/label")
GameShow = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[3]/td[4]/label")

History = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[4]/td[1]/label")
Horror = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[4]/td[2]/label")
Music = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[4]/td[3]/label")
Musical = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[4]/td[4]/label")

Mystery = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[5]/td[1]/label")
News = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[5]/td[2]/label")
RealityTV = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[5]/td[3]/label")
Romance = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[5]/td[4]/label")

SciFi = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[6]/td[1]/label")
Sport = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[6]/td[2]/label")
TalkShow = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[6]/td[3]/label")
Thriller = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[6]/td[4]/label")

War = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[7]/td[1]/label")
Western = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/div[6]/div[2]/table/tbody/tr[7]/td[2]/label")

search = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/form/div/p[3]/button")

Crime.click()
# Comedy.click()
search.click()

for x in range(50):
    show1 = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[" + str(x+1) + "]/div[3]/h3/a")
    print(str(x+1) + ": " + show1.text)

# show1 = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[1]/div[3]/h3/a")
# show2 = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[2]/div[3]/h3/a")
# show3 = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[3]/div[3]/h3/a")
# show4 = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[4]/div[3]/h3/a")
# show5 = browser.find_element(By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div/div[5]/div[3]/h3/a")

# print(show1.text)
# print(show2.text)
# print(show3.text)
# print(show4.text)
# print(show5.text)
