'''
Сделайте сценарий для добавления нового товара (продукта) в учебном приложении litecart (в админке).
Для добавления товара нужно открыть меню Catalog, в правом верхнем углу нажать кнопку "Add New Product", заполнить поля с информацией о товаре и сохранить.
Достаточно заполнить только информацию на вкладках General, Information и Prices. Скидки (Campains) на вкладке Prices можно не добавлять.
Переключение между вкладками происходит не мгновенно, поэтому после переключения можно сделать небольшую паузу (о том, как делать более правильные ожидания, будет рассказано в следующих занятиях).
Картинку с изображением товара нужно уложить в репозиторий вместе с кодом. При этом указывать в коде полный абсолютный путь к файлу плохо, на другой машине работать не будет. Надо средствами языка программирования преобразовать относительный путь в абсолютный.
После сохранения товара нужно убедиться, что он появился в каталоге (в админке). Клиентскую часть магазина можно не проверять.
'''
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

import faker
from faker.providers import internet
from faker.providers import address
from faker.providers import phone_number
from faker.providers import lorem
import  time

wd = webdriver.Chrome()

wait = WebDriverWait(wd, 30) # seconds
wd.get('http://litecart.stqa.ru/admin/')
wd.find_element_by_name('username').send_keys('admin')
wd.find_element_by_name('password').send_keys('0b7dba1c77df25bf0')
wd.find_element_by_name('login').click()

wd.find_element_by_link_text('Catalog').click()
wd.find_element_by_css_selector('#content > div:nth-child(2) > a:nth-child(2)').click()

time.sleep(2)
fake = faker.Faker()
name = fake.bothify(text="???????????", letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
code = fake.bothify(text="###-???", letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
keywords = fake.bothify(text="???, ??????, ??????", letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
short_descr = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
descr = fake.text()
title = name
meta = short_descr
SKU = fake.bothify(text="###-?##-##?", letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
GTN = fake.bothify(text="#############", letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
TARIC = fake.bothify(text="######## ## ####", letters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

wd.find_element_by_css_selector("input[name='name[en]']").send_keys(name)
wd.find_element_by_css_selector("input[name='code']").send_keys(code)

elements = wd.find_elements_by_css_selector("input[name='categories[]']")
for element in elements:
    element.click()

select.Select(wd.find_element_by_css_selector("select[name='default_category_id']")).select_by_value('2')

wd.find_element_by_css_selector("input[value='1-3']").click()
wd.find_element_by_css_selector("input[name=quantity]").clear()
wd.find_element_by_css_selector("input[name=quantity]").send_keys("12345,44")
wd.find_element_by_css_selector("input[name='new_images[]']").send_keys(os.getcwd()+"/duck.jpg")

wd.find_element_by_xpath('//*[@id="content"]/form/div/ul/li[2]/a').click()
time.sleep(1)
select.Select(wd.find_element_by_css_selector("select[name='manufacturer_id']")).select_by_value('1')
wd.find_element_by_css_selector("input[name=keywords]").send_keys(keywords)
wd.find_element_by_css_selector("input[name='short_description[en]']").send_keys(short_descr)
wd.execute_script("document.querySelector('div.trumbowyg-editor').innerText = arguments[0]", descr)
wd.find_element_by_css_selector("input[name='head_title[en]']").send_keys(title)
wd.find_element_by_css_selector("input[name='meta_description[en]']").send_keys(meta)

wd.find_element_by_xpath('//*[@id="content"]/form/div/ul/li[3]/a').click()
time.sleep(1)
wd.find_element_by_css_selector("input[name=sku]").send_keys(SKU)
wd.find_element_by_css_selector("input[name=gtin]").send_keys(GTN)
wd.find_element_by_css_selector("input[name=taric]").send_keys(TARIC)

wd.find_element_by_css_selector("button[name=save]").click()
wd.quit()


