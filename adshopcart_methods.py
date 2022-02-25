import sys
import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r'C:\Users\asus\PycharmProjects\python-cctb\chromedriver.exe')

# s = Service(executable_path='./chromedriver')
# driver = webdriver.Chrome(service=s)

def setUp():
    print(f'Test start at: {datetime.datetime.now()}')
    driver.maximize_window()
    # Let's wait for the browser response in general
    driver.implicitly_wait(30)

    driver.get(locators.moodle_url)

    # Checking that we're non the correct URL address and we're seeing correct titile
    if driver.current_url == locators.moodle_url and driver.title == ' Advantage Shopping':
        print(f'We are at Advantage Shopping homepage -- {driver.current_url}')
        print(f'We are seeing title message -- " Advantage Shopping"')
    else:
        print(f'We are not at Advantage Shopping homepage. Check your code!')
        # driver.close()
        # driver.quit()


def tearDown():
    if driver is not None:
        print(f'---------------------')
        print(f'Test completed at: {datetime.datetime.now()}')
        driver.close()
        driver.quit()

# setUp()
# tearDown()
