'''
Сделайте сценарии, которые проверяют сортировку стран и геозон (штатов) в учебном приложении litecart.

1) на странице http://localhost/litecart/admin/?app=countries&doc=countries
а) проверить, что страны расположены в алфавитном порядке
б) для тех стран, у которых количество зон отлично от нуля -- открыть страницу этой страны и там проверить, что зоны расположены в алфавитном порядке

2) на странице http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones
зайти в каждую из стран и проверить, что зоны расположены в алфавитном порядке
'''
import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

wd = webdriver.Chrome()

wait = WebDriverWait(wd, 30) # seconds
wd.get('http://litecart.stqa.ru/admin/')
wd.find_element_by_name('username').send_keys('admin')
wd.find_element_by_name('password').send_keys('0b7dba1c77df25bf0')
wd.find_element_by_name('login').click()
wd.get("http://litecart.stqa.ru/admin/?app=countries&doc=countries")

root_elements = wd.find_elements_by_css_selector("[name=countries_form] a:not([title])")

root_links = []
for root_element in root_elements:
    root_links.append(root_element.text)

zones = wd.find_elements_by_css_selector("[name=countries_form] td:nth-child(6)")
zone_links = []
for zone in zones:
    zone_links.append(zone.text)

i = 0

if root_links == sorted(root_links):
    print("countries equal countries sorted")
else:
    print("countries not equal countries sorted")

for root_link in root_links:
    #print(root_link, zone_links[i])
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[name="disable"]')))
    if int(zone_links[i]) != 0:
        wd.find_element_by_link_text(root_link).click()
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        sub_elements = wd.find_elements_by_css_selector("form td:nth-child(3)")
        sub_text = []
        for sub_element in sub_elements:
            if sub_element.text != "":
                sub_text.append(sub_element.text)

        if sub_text == sorted(sub_text):
            print("\t zones is equal sorted")
        else:
            print("\t zones is not equal sorted")

        wd.back()
    i += 1

wd.get("http://litecart.stqa.ru/admin/?app=geo_zones&doc=geo_zones")
root_elements = wd.find_elements_by_css_selector("[name=geo_zones_form] a:not([title])")

root_links = []
for root_element in root_elements:
    root_links.append(root_element.text)

for root_link in root_links:
    wd.find_element_by_link_text(root_link).click()

    sub_elements = wd.find_elements_by_css_selector("[name=form_geo_zone] td:nth-child(3) option[selected]")
    sub_text = []
    for sub_element in sub_elements:
        sub_text.append(sub_element.text)

    if sub_text == sorted(sub_text):
        print(root_link, "\t zones is equal sorted")
    else:
        print(root_link, "\t zones is not equal sorted")
    wd.back()


wd.quit()
sys.exit()
