'''
если у всех товаров стикеры есть -- сценарий должен завершиться успешно. если у какого-то товара стикера нет -- сценарий должен падать. выводить что-то на консоль или не выводить -- это уже ваше дело
'''

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

wd = webdriver.Chrome()
wait = WebDriverWait(wd, 10) # seconds
wd.get("http://litecart.stqa.ru")

root_elements = wd.find_elements_by_css_selector("li.product > a")

i = 0
for root_element in root_elements:
    have_sticker = root_element.find_elements_by_css_selector("div.sticker")
    if len(have_sticker) == 1:
        i += 1


    ''' test
    if len(have_sticker) == 0:
        print(root_element.get_attribute("title"), "\t no sticker")
    elif len(have_sticker) == 1:
        print(root_element.get_attribute("title"), "\t 1 sticker")
    else:
        print(root_element.get_attribute("title"), "\t more then 1 sticker")
    '''
    ''' 
    if len(have_sticker) == 1:
        print(root_element.get_attribute("title"), "\t 1 sticker")
    '''

if len(root_elements) != i:
    print("Не у всех товаров есть стикер")
else:
    print("У всех товаров есть стикер")

wd.quit()



