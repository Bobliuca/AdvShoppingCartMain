import sys
import datetime
import adshopcart_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(r':\Users\asus\PycharmProjects\python-cctb\chromedriver.exe')

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
        sleep(1)
    else:
        print('register failed! check your code.')

    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(1)



def check_user_created():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
    sleep(0.8)
    if driver.current_url == locators.adshopcart_users_main_page:
        assert driver.find_element(By.ID, 'myAccountContainer').is_displayed()
        sleep(0.25)
        print('User is created!')
        if driver.find_element(By.XPATH, f'//label[contains(., "{locators.first_name}")]'):
            print(f'New User "{locators.first_name}" "{locators.last_name}" is created!')
            print('--- Test Scenario: Check user created --- is passed')
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[2]').click()
    sleep(.5)
    if driver.find_element(By.XPATH, "//label[contains(.,'- No orders -')]").is_displayed():
        print(f' --- NO ORDERS ---')

def log_out():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(1.5)
    driver.find_element(By.ID, 'menuUser').click()
    sleep(3)
    if driver.find_element(By.ID, 'sign_in_btnundefined').is_displayed():
        print(f'"{locators.new_username}" is successfully logout at: {datetime.datetime.now()}!')
    else:
        print(f'!!!!!!!!!!!"{locators.new_username}" is not successfully logout at: {datetime.datetime.now()}!')




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
        sleep(1)

def delete_a_new_user():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[1]').click()
    sleep(1)
    if driver.current_url == locators.adshopcart_users_main_page:
        assert driver.find_element(By.CLASS_NAME, 'deleteBtnText').is_displayed()
        sleep(0.25)
        driver.find_element(By.CLASS_NAME, 'deleteBtnText').click()
        sleep(1.5)
        if driver.find_element(By.ID, 'deleteAccountPopup').is_displayed():
            driver.find_element(By.XPATH, '//*[@id="deleteAccountPopup"]/div[3]/div[1]').click()
            print(f'-------New user is deleted.')
        else:
            print('!!!!!!!!!!!!!!!New user deleted failed.' )
    sleep(1.5)


def check_user_deleted():
    driver.get(locators.adshopcart_url)
    sleep(1.5)
    if driver.current_url == locators.adshopcart_url:
        driver.find_element(By.ID, 'menuUser').click()
        sleep(1)
        assert driver.find_element(By.ID, 'sign_in_btnundefined').is_displayed()
        sleep(0.5)
        driver.find_element(By.NAME, 'username').send_keys(locators.new_username)
        sleep(0.25)
        driver.find_element(By.NAME, 'password').send_keys(locators.new_password)
        sleep(0.25)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(1)
        if driver.find_element(By.XPATH, '//label[contains(., "Incorrect")]'):
            print(f'The User "{locators.new_username}" has been deleted! Test Passed!')
            print('Test Scenario: Check the new user deleted --- is passed!')

    # breakpoint()
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












# setUp()
# create_new_user()
# log_out()
# log_in()
# check_user_created()
# delete_a_new_user()
# check_user_deleted()
# tearDown()