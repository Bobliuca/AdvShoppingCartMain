import sys
import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(r'C:\Users\asus\PycharmProjects\python-cctb\chromedriver.exe')

s = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=s)

def setUp():

    print(f'Test start at: {datetime.datetime.now()}')
    driver.maximize_window()

    driver.implicitly_wait(30)
    driver.get(locators.adshopcart_url)
    sleep(2)

    if driver.current_url == locators.adshopcart_url and driver.find_element(By.XPATH, '//title[contains(., "Advantage Shopping")]'):
        print(f'We are at Advantage Shopping homepage -- {driver.current_url}')
        print(f'We are seeing title message -- "Advantage Shopping"')
    else:
        print(f'We are not at Advantage Shopping homepage. Check your code!')


def tearDown():
    if driver is not None:
        print(f'---------------------')
        print(f'Test completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()