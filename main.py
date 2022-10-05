from email import header
from tkinter import BROWSE
from wsgiref.headers import Headers
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

starturl = "https://exoplanets.nasa.gov/exoplanet-catalog/"
browser = webdriver.Chrome("C:\Users\ramsh\OneDrive\Desktop\whitehat\c127\chromedriver.exe")
browser.get(starturl)
time.sleep(10)

def scrap():
    headers = ["name","light_years_from_earth","planet_mars","stellar_magnitude","discovery_data"]
    planet_data = []
    for i in range(0,428):
        soup = BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all('ul',attrs={"class","exoplanet"}):
            li_tags = ul_tag.find_all("li")
            temp_list = []
            for index,li_tag in enumerate(li_tags):
                if index == 0 :
                    temp_list.append(li_tag.find_all('a')[0].contents[0])
                else :
                    try :
                        temp_list.append(li_tag.contents[0])

                    except :
                        temp_list.append('')
            planet_data.append(temp_list)
        browser.find_element_by_XPATH('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open('scrapper_2.csv','w')as f:
        csvWritter = csv.writer(f)
        csvWritter.writerow(headers)
        csvWritter.writerows(planet_data)


scrap()

