from bs4 import BeautifulSoup

def get_total_withdraw(driver):
    page = 1
    total_withdraw = 0

    while True:
        driver.get('https://www.winamax.fr/account/history.php?to_display=withdrawals&history_date_from_day=01&history_date_from_month=01&history_date_from_year=2010&history_date_to_day=31&history_date_to_month=12&history_date_to_year=2021&order_by=&page=' + str(page))
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.find('table', attrs={'class':'no-break-word'})
        rows = table.find_all('tr')
        rows.pop(0)

        if len(rows) <= 1:
            break
        for row in rows:
            data = row.find_all('td')
            total_withdraw += float(data[2].text.replace(',', '.'))
        page += 1

    return total_withdraw

def get_total_deposits(driver):
    page = 1
    total_deposits = 0

    while True:
        url = "https://www.winamax.fr/mon-compte_historique-de-compte?to_display=deposits&history_date_from_day=01&history_date_from_month=01&history_date_from_year=2010&history_date_to_day=31&history_date_to_month=12&history_date_to_year=2021&order_by=&page=" + str(page)
        driver.get(url)
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.find('table', attrs={'class':'no-break-word'})
        rows = table.find_all('tr')
        rows.pop(0)

        if len(rows) <= 1:
            break
        for row in rows:
            data = row.find_all('td')
            total_deposits += float(data[2].text.replace(',', '.'))
        page += 1
    
    return total_deposits