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

def create_new_user():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    driver.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
    sleep(0.25)
    assert driver.find_element(By.ID, 'registerPage').is_displayed()
    print('We can create new account now!')
    sleep(0.25)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
    print(f'-------user: "{locators.new_username}".')
    sleep(0.25)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    print(f'-------email: "{locators.email}".')
    sleep(0.25)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.new_password)
    print(f'-------password: "{locators.new_password}".')
    sleep(0.25)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
    sleep(0.25)
    # Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_value("Canada")
    # sleep(0.25)
    # driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    # sleep(0.25)
    # driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    # sleep(0.25)
    # driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
    # sleep(0.25)
    # driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.province)
    # sleep(0.25)
    if not driver.find_element(By.ID, 'register_btnundefined').click():
        driver.find_element(By.NAME, 'i_agree').click()
        sleep(0.25)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(0.25)


def check_user_created():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'My account').click()
    sleep(0.25)
    if driver.current_url == locators.adshopcart_users_main_page:
        assert driver.find_element(By.CLASS_NAME, 'MY_ACCOUNT').is_displayed()
        sleep(0.25)
        # driver.find_element(By.XPATH, "//label[contains(.,'Confirm password')]")
        if driver.find_element(By.XPATH, f'//td[contains(., "{locators.first_name}")]'):
            print(f'Welcome! New User "{locators.first_name}" "{locators.last_name}" is created!')
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'My orders').click()
    sleep(.25)
    if driver.find_element(By.XPATH, "//label[contains(.,'- No orders -')]").is_displayed():
        print(f' --- NO ORDERS ---')

def log_out():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    # driver.find_element(By.XPATH, "//div[@label='Sign_out')]").click()
    # driver.find_element(By.XPATH, "//label[contains(.,'Sign_out')]").click()
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(0.5)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    if driver.find_element(By.ID, 'sign_in_btnundefined').is_displayed():
        print(f'"{locators.new_username}" is successfully logout at: {datetime.datetime.now()}!')
    else:
        print(f'"{locators.new_username}" is not successfully logout at: {datetime.datetime.now()}!')

# log_in(locators.moodle_username, locators.moodle_password)


def log_in():
    driver.get(locators.adshopcart_url)
    if driver.current_url == locators.adshopcart_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)
        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        sleep(0.25)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(0.25)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(0.25)

def delete_a_new_user():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
    sleep(0.25)
    if driver.current_url == locators.adshopcart_users_main_page:
        assert driver.find_element(By.CLASS_NAME, 'MY_ACCOUNT').is_displayed()
        sleep(0.25)
        driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
        print(f'-------New user is deleted. at {datetime.datetime.now()}! ')

def check_user_deleted():
    driver.get(locators.adshopcart_url)
    if driver.current_url == locators.adshopcart_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(2)
        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        sleep(0.25)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(0.25)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(0.25)
        if driver.find_element(By.ID, 'signInResultMessage'):
            print(f'The User "{locators.new_username}" has deleted! .')

    # breakpoint()

# setUp()
# create_new_user()
# log_out()
# log_in()
# check_user_created()
# delete_a_new_user()
# check_user_deleted()
# tearDown()