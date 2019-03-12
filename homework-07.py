from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

wd = webdriver.Chrome()

wait = WebDriverWait(wd, 10) # seconds
wd.get('http://litecart.stqa.ru/admin/')
wd.find_element_by_name('username').send_keys('admin')
wd.find_element_by_name('password').send_keys('0b7dba1c77df25bf0')
wd.find_element_by_name('login').click()

root_elements = wd.find_elements_by_css_selector("ul#box-apps-menu li > a")

root_links = []
for root_element in root_elements:
    root_links.append(root_element.text)

for root_link in root_links:
    print("Root_link", root_link)
    wd.find_element_by_link_text(root_link).click()
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

    sub_elements = wd.find_elements_by_css_selector("ul#box-apps-menu li > ul > li > a > span")
    sub_links = []

    for sub_element in sub_elements:
        sub_links.append(sub_element.text)

    for sub_link in sub_links:
        print(root_link, sub_link)
        wd.find_element_by_link_text(sub_link).click()
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
wd.quit()