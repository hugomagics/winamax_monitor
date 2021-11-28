import os
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from connection import wina_connect
from dotenv import load_dotenv

load_dotenv()

print("Connection en cours")
driver = wina_connect(os.getenv('EMAIL'), os.getenv('PASSWORD'), os.getenv('BIRTH_DATE'))
print("connectée !")

page_data = []
pages = []
page = 1
total_deposits = 0

while True:
    page_data = []
    url = "https://www.winamax.fr/mon-compte_historique-de-compte?to_display=deposits&history_date_from_day=01&history_date_from_month=01&history_date_from_year=2010&history_date_to_day=31&history_date_to_month=12&history_date_to_year=2021&order_by=&page=" + str(page)
    driver.get(url)
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    table = soup.find('table', attrs={'class':'no-break-word'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        page_data.append([ele for ele in cols if ele])
    if (len(page_data) == 1):
        break
    pages.append(page_data)
    page += 1

for page in pages:
    for deposit in page:
        if (len(deposit) > 0):
            total_deposits += float(deposit[2].replace(',', '.'))

print("Total deposit sur winamax : " + str(int(total_deposits)) )

page_data = []
pages = []
page = 1
total_withdraw = 0

while True:
    page_data = []
    driver.get('https://www.winamax.fr/account/history.php?to_display=withdrawals&history_date_from_day=01&history_date_from_month=01&history_date_from_year=2010&history_date_to_day=31&history_date_to_month=12&history_date_to_year=2021&order_by=&page=' + str(page))
    soup = BeautifulSoup(driver.page_source, "html.parser")
    table = soup.find('table', attrs={'class':'no-break-word'})
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        page_data.append([ele for ele in cols if ele])
    if (len(page_data) == 1):
        break
    pages.append(page_data)
    page += 1

for page in pages:
    for withdraw in page:
        if (len(withdraw) > 0):
            total_withdraw += float(withdraw[2].replace(',', '.'))

print("Total withdraw sur winamax : " + str(int(total_withdraw)))
print("total gagné = " + str(int(total_withdraw - total_deposits)))
