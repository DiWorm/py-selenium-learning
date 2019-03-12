from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

wd = webdriver.Chrome()
wait = WebDriverWait(wd, 10) # seconds
wd.get("http://litecart.stqa.ru")

root_elements = wd.find_elements_by_css_selector("div.content a.link")
i = 0
for root_element in root_elements:
    have_sticker = root_element.find_elements_by_css_selector("div.sticker")
    if len(have_sticker) == 0:
        print(root_element.get_attribute("title"), "\t no sticker")
    elif len(have_sticker) == 1:
        print(root_element.get_attribute("title"), "\t 1 sticker")
    else:
        print(root_element.get_attribute("title"), "\t more then 1 sticker")
wd.quit()



