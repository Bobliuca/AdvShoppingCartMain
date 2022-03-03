import sys
import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

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

    if driver.current_url == locators.adshopcart_url and driver.title.endswith('Advantage Shopping'):
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

def check_homepage():
    if driver.find_element(By.ID, 'speakersTxt') \
            and driver.find_element(By.ID, 'tabletsTxt') \
            and driver.find_element(By.ID, 'laptopsTxt') \
            and driver.find_element(By.ID, 'miceTxt') \
            and driver.find_element(By.ID, 'headphonesTxt'):
        print('_______SPEAKERS, TABLETS, HEADPHONES, LAPTOPS, MICE___________are displayed')
    else:
        print('_______SPEAKERS, TABLETS, HEADPHONES, LAPTOPS, MICE___________are not displayed')
    sleep(.25)
    driver.find_element(By.LINK_TEXT, 'SPECIAL OFFER').click()
    sleep(.25)
    if driver.find_element(By.ID, 'special_offer_items').is_displayed():
        print('"SPECIAL OFFER" button is clickable!')
    else:
        print('SPECIAL OFFER button is not clickable!')
    driver.find_element(By.LINK_TEXT, 'POPULAR ITEMS').click()
    sleep(.25)
    if driver.find_element(By.ID, 'popular_items').is_displayed():
        print('"POPULAR ITEMS" button is clickable!')
    else:
        print('"POPULAR ITEMS" button is not clickable!')
    driver.find_element(By.LINK_TEXT, 'CONTACT US').click()
    sleep(.25)
    if driver.find_element(By.ID, 'contact_us').is_displayed():
        print('"CONTACT US" button is clickable!')
    else:
        print('CONTACT US button is not clickable!')
    sleep(.25)
    if driver.find_element(By.XPATH, '//span[contains(., "dvantage")]').is_displayed():
        print('The dvantageDEMO Logo is displayed!')
    else:
        print('Logo error')

def fill_contact_infor():
    driver.find_element(By.ID, 'contact_us').click()
    Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Laptops')
    sleep(.25)
    assert driver.find_element(By.XPATH, '//*[@id="supportCover"]/div[2]/sec-form/div[1]/div/sec-view[1]\
    /div/select/option[2]').is_displayed()
    driver.find_element(By.XPATH, '//*[@id="supportCover"]\
    /div[2]/sec-form/div[1]/div/sec-view[3]/div/input').send_keys(locators.email)
    sleep(.5)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.description)
    sleep(.5)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(.25)
    if driver.find_element(By.ID, 'registerSuccessCover').is_displayed():
        print('------------------Contact Us function test passed!---------------')
    else:
        print('!!!!!!!!!!!!Contact Us function test failed!')








setUp()
check_homepage()
fill_contact_infor()
tearDown()