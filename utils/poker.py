from bs4 import BeautifulSoup

def get_all_poker(driver):
    page = 1
    played = 0
    won = 0

    while True:
        url = "https://www.winamax.fr/account/history.php?to_display=sitngo&history_date_from_day=01&history_date_from_month=01&history_date_from_year=2010&history_date_to_day=31&history_date_to_month=12&history_date_to_year=2022&order_by=&page=" + str(page)
        driver.get(url)
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.find('table', attrs={'class':'no-break-word'})
        try:
            rows = table.find_all('tr')
        except:
            break

        for row in rows[3::2]:
            data = row.find_all('td')

            if data[4].text.strip() == "Expresso":
                played += float(data[2].text.replace(',', '.'))
                try:
                    won += float(data[6].text.replace('€', '').strip().replace(',', '.'))
                except:
                    pass
        page += 1

    print("\texpresso win : " + str(int(won) - int(played)) + " € for played " + str(int(played)) + " €")
    return 0