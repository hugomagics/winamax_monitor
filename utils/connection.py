from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def wina_connect(email, pwd, birth_date):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)

    driver.get("https://www.winamax.fr/")
    sleep(1)
    driver.find_element(By.ID,"tarteaucitronPersonalize2").click()
    sleep(1)
    driver.find_element(By.ID,"login-link").click()
    sleep(1)

    driver.switch_to.frame('iframe-login')
    sleep(1)
    driver.find_element(By.CLASS_NAME, "iViUcq").send_keys(email)
    driver.find_element(By.CLASS_NAME, "sc-kEYyzF").send_keys(pwd)
    driver.find_element(By.CLASS_NAME, "gLzxCe").click()
    sleep(1)
    bd = driver.find_elements(By.CLASS_NAME, "sc-VigVT")
    bd[0].send_keys(birth_date.split('/')[0])
    bd[1].send_keys(birth_date.split('/')[1])
    bd[2].send_keys(birth_date.split('/')[2])
    driver.find_element(By.CLASS_NAME, "gLzxCe").click()
    sleep(3)
    
    return (driver)