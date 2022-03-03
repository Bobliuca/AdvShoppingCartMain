from faker import Faker

fake = Faker(locale='en_CA')
adshopcart_url = 'https://advantageonlineshopping.com/#/'
adshopcart_users_main_page = 'https://advantageonlineshopping.com/#/myAccount'
description = fake.sentence(nb_words=20)
new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake.last_name()
full_name = f'{first_name} {last_name}'
email = fake.email()

city = fake.city()
pic_desc = fake.user_name()
phonetic_name = fake.user_name()
list_of_interests = [new_username, new_password, full_name, email, city]
phone = fake.phone_number()
mobile_phone = fake.phone_number()
address = fake.address()
# address = fake.address().replace("\n", "")
province = fake.province()


# old_username = fake.user_name()
# new_username = old_username[0:14]
# old_username = fake. user_name()
# if len(old_username) >= 6:
#     old_username = old_username[0:6]

