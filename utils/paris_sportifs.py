from bs4 import BeautifulSoup

def get_all_bets(driver):
    page = 1
    played = 0
    won = 0

    while True:
        url = "https://www.winamax.fr/account/history.php?to_display=betting&history_date_from_day=01&history_date_from_month=01&history_date_from_year=2010&history_date_to_day=31&history_date_to_month=12&history_date_to_year=2022&filter_type=&filter_state=&order_by=&page=" + str(page)
        driver.get(url)
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.find('table', attrs={'class':'no-break-word'})
        rows = table.find_all('tr')

        if (len(rows) <= 3):
            break

        for row in rows[3::2]:
            data = row.find_all('td')
            etat = data[3].text.strip()
            played += float(data[4].text.replace(',', '.'))
            try:
                won += float(data[5].text.replace(',', '.'))
            except:
                pass
        page += 1

    print("\tbets win : " + str(int(won) - int(played)) + " € for played " + str(int(played)) + " €")
    return 0