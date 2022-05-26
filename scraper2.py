from urllib import request
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import requests

url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser=webdriver.Chrome("C:/Users/Admin/Desktop/Purvaa coding folder/chromedriver")
browser.get(url)
time.sleep(10)
def scrape_data():
    headers=["Name","Distance","Mass","Radius"]
    brown_dwarfs=[]

    page=requests.get(url)
    soup=BeautifulSoup(page.text,"html.parser")
    star_table=soup.find_all('table')
    table_row=star_table[5].find_all('tr')

    for tr_tags in table_row:
        temp_list=[]
        td_tags=tr_tags.find_all('td')

        try:
            temp_list.append(td_tags[0].text.strip())
            temp_list.append(td_tags[5].text.strip())
            temp_list.append(td_tags[7].text.strip())
            temp_list.append(td_tags[8].text.strip())

        except:
            temp_list.append('')    

        brown_dwarfs.append(temp_list)

    
    with open("scraper.csv" , "w") as p :
        csv_writer=csv.writer(p)
        csv_writer.writerow(headers)
        csv_writer.writerows(brown_dwarfs)

scrape_data()