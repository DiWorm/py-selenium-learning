import sys
from selenium import webdriver

wd = webdriver.Chrome()
wd.get('http://litecart.stqa.ru/admin/')
wd.find_element_by_name('username').send_keys("admin")
wd.find_element_by_name('password').send_keys("0b7dba1c77df25bf0")
wd.find_element_by_name('login').click()
wd.quit()
sys.exit()