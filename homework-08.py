from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

wd = webdriver.Chrome()
wait = WebDriverWait(wd, 10) # seconds
wd.get("http://litecart.stqa.ru")

root_elements = wd.find_elements_by_css_selector("div.content a.link")


ducks = []
for root_element in root_elements:
    ducks.append(root_element.text)

print(ducks)


