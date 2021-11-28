from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def wina_connect(email, pwd, birth_date):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('window-size=1920x1080')

    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.winamax.fr/")
    sleep(2)
    element = driver.find_element(By.ID,"login-link")
    element.click()
    sleep(2)


    # email
    actions = ActionChains(driver)
    actions.move_by_offset(1350, 175).click().perform()
    actions.send_keys(email).perform()
    actions.move_by_offset(0, 85).click().perform()
    actions.send_keys(pwd).perform()
    actions.move_by_offset(0, 85).click().perform()
    sleep(1)

    jour = birth_date.split('/')[0]
    mois = birth_date.split('/')[1]
    année = birth_date.split('/')[2]

    # date = ActionChains(driver)
    actions.move_by_offset(-150, -170).click().perform()
    actions.send_keys(jour).perform()
    actions.move_by_offset(100, 0).click().perform()
    actions.send_keys(mois).perform()
    actions.move_by_offset(100, 0).click().perform()
    actions.send_keys(année).perform()
    actions.move_by_offset(0, 55).click().perform()
    sleep(1)
    return (driver)