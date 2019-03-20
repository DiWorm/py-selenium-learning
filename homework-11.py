'''
Сделайте сценарий для регистрации нового пользователя в учебном приложении litecart (не в админке, а в клиентской части магазина).
Сценарий должен состоять из следующих частей:
1) регистрация новой учётной записи с достаточно уникальным адресом электронной почты (чтобы не конфликтовало с ранее созданными пользователями, в том числе при предыдущих запусках того же самого сценария),
2) выход (logout), потому что после успешной регистрации автоматически происходит вход,
3) повторный вход в только что созданную учётную запись,
4) и ещё раз выход.
В качестве страны выбирайте United States, штат произвольный. При этом формат индекса -- пять цифр.
Можно оформить сценарий либо как тест, либо как отдельный исполняемый файл.
Проверки можно никакие не делать, только действия -- заполнение полей, нажатия на кнопки и ссылки. Если сценарий дошёл до конца, то есть созданный пользователь смог выполнить вход и выход -- значит создание прошло успешно.
В форме регистрации есть капча, её нужно отключить в админке учебного приложения на вкладке Settings -> Security.
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

import faker
from faker.providers import internet
from faker.providers import address
from faker.providers import phone_number

wd = webdriver.Chrome()
wait = WebDriverWait(wd, 30) # seconds
wd.get('http://litecart.stqa.ru/en/create_account')

f = faker.Faker()
f.add_provider(internet)
f.add_provider(address)
f.add_provider(phone_number)

first_name = f.first_name()
last_name =  f.last_name()
login = f.user_name()
street = f.street_address()
email = f.email()
phone = f.msisdn()
postal_code = f.postcode_in_state()
city = f.city()

wd.find_element_by_css_selector("span.select2-selection__rendered").click()
wd.find_element_by_css_selector("input.select2-search__field").send_keys("United States",Keys.ENTER)

wd.find_element_by_css_selector("[name=firstname]").send_keys(first_name)
wd.find_element_by_css_selector("[name=lastname]").send_keys(last_name)

wd.find_element_by_css_selector("[name=address1]").send_keys(street)
wd.find_element_by_css_selector("[name=postcode]").send_keys(postal_code)
wd.find_element_by_css_selector("[name=city]").send_keys(city)
wd.find_element_by_css_selector("[name=email]").send_keys(email)
wd.find_element_by_css_selector("[name=phone]").send_keys(phone)

wd.find_element_by_css_selector("[name=password]").send_keys(first_name)
wd.find_element_by_css_selector("[name=confirmed_password]").send_keys(first_name)

wd.find_element_by_css_selector("[type=submit]").click()
wd.find_element_by_link_text("Logout").click()

wd.find_element_by_css_selector("[name=email]").send_keys(email)
wd.find_element_by_css_selector("[name=password").send_keys(first_name)
wd.find_element_by_link_text("Login").click()

if wd.find_element_by_css_selector("h1.title").text == "Login":
    print("Register and Login Done")
else:
    print("Somthing wrong")

wd.quit()