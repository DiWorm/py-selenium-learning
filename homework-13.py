'''
Сделайте сценарий для добавления товаров в корзину и удаления товаров из корзины.

1) открыть главную страницу
2) открыть первый товар из списка
2) добавить его в корзину (при этом может случайно добавиться товар, который там уже есть, ничего страшного)
3) подождать, пока счётчик товаров в корзине обновится
4) вернуться на главную страницу, повторить предыдущие шаги ещё два раза, чтобы в общей сложности в корзине было 3 единицы товара
5) открыть корзину (в правом верхнем углу кликнуть по ссылке Checkout)
6) удалить все товары из корзины один за другим, после каждого удаления подождать, пока внизу обновится таблица
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
wd = webdriver.Chrome()
wait = WebDriverWait(wd, 10) # seconds
wd.get('http://litecart.stqa.ru/en/')

i = 1
for _ in range(3):
    if i <= 3:
        product = wd.find_element_by_css_selector("div#box-campaigns li.product a.link")
        product.click()

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        if wd.find_element_by_css_selector("select[name='options[Size]']"):
            select.Select(wd.find_element_by_css_selector("select[name='options[Size]']")).select_by_value('Medium')

        wd.find_element_by_css_selector("[name='add_cart_product'").click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'.quantity'), str(i)))
        if i < 3:
            i += 1
            wd.back()
        else:
            wd.find_element_by_css_selector("div#cart > a.link").click()
            inp = int(wd.find_element_by_css_selector('input[name=quantity]').get_attribute('value'))
            for _ in range(3):
                inp -= 1
                if inp != 0:
                    wd.find_element_by_css_selector('input[name=quantity]').clear()
                    wd.find_element_by_css_selector('input[name=quantity]').send_keys(inp)
                    wd.find_element_by_css_selector('[name=update_cart_item]').click()
                    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="order_confirmation-wrapper"]/table/tbody/tr[2]/td[1]'), str(inp)))
                else:
                    print('it works!')
                    wd.quit()