from faker import Faker

fake = Faker(locale='en_CA')
adshopcart_url = 'https://advantageonlineshopping.com/#/'
# adshopcart_login_url = 'http://52.39.5.126/login/index.php'
adshopcart_users_main_page = 'https://advantageonlineshopping.com/#/myAccount'
# adshopcart_username = 'boliu'
# adshopcart_password = 'Nerdca78*'
# adshopcart_dashboard_url = 'http://52.39.5.126/my/'
new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()

city = fake.city()  #country = fake.country() 任意国家 #country= fake.current_country() 当前国家
pic_desc = fake.user_name()
phonetic_name = fake.user_name()
list_of_interests = [new_username, new_password, full_name, email, city]
phone = fake.phone_number()
mobile_phone = fake.phone_number()
address = fake.address()
# address = fake.address().replace("\n", "")
province = fake.province()

