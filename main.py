import sys
sys.dont_write_bytecode = True

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv

from utils.connection import wina_connect
from utils.totals import get_total_deposits, get_total_withdraw
from utils.paris_sportifs import get_all_bets
from utils.poker import get_all_poker

load_dotenv()

def winamax():
    print("Connection to your account " + os.getenv("EMAIL"))
    driver = wina_connect(os.getenv('EMAIL'), os.getenv('PASSWORD'), os.getenv('BIRTH_DATE'))
    print("Connected !\n")

    total_deposit = get_total_deposits(driver)
    total_withdraw = get_total_withdraw(driver)

    print("[looking for expressos and sports bets]")
    get_all_bets(driver)
    get_all_poker(driver)
    print()

    print("[accounts totals]")
    print("\tdeposit on winamax : " + str(total_deposit) + " €")
    print("\twithdraw on winamax : " + str(int(total_withdraw)) + " €")
    print("\twon = " + str(int(total_withdraw - total_deposit)) + " €")

    # close the browser window
    driver.close()

if __name__ == '__main__':
    winamax()