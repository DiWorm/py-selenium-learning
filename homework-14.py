'''
1) зайти в админку
2) открыть пункт меню Countries (или страницу http://localhost/litecart/admin/?app=countries&doc=countries)
3) открыть на редактирование какую-нибудь страну или начать создание новой
4) возле некоторых полей есть ссылки с иконкой в виде квадратика со стрелкой -- они ведут на внешние страницы и открываются в новом окне, именно это и нужно проверить.
Конечно, можно просто убедиться в том, что у ссылки есть атрибут target="_blank". Но в этом упражнении требуется именно кликнуть по ссылке, чтобы она открылась в новом окне, потом переключиться в новое окно, закрыть его, вернуться обратно, и повторить эти действия для всех таких ссылок.
Не забудьте, что новое окно открывается не мгновенно, поэтому требуется ожидание открытия окна.
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

wd = webdriver.Chrome()
wd.implicitly_wait(30)

wd.get('http://litecart.stqa.ru/admin/')
wd.find_element_by_name('username').send_keys('admin')
wd.find_element_by_name('password').send_keys('0b7dba1c77df25bf0')
wd.find_element_by_name('login').click()
wd.get("http://litecart.stqa.ru/admin/?app=countries&doc=countries")
wd.find_element_by_link_text('Albania').click()
links = wd.find_elements_by_css_selector("td > a:not(#address-format-hint)")
count_links = len(links)
main_window = wd.current_window_handle
i = 0
new_window = []
for i in range(0, count_links):
    links[i].click()
    new_window = wd.window_handles
    new_window.remove(main_window)
    #Как писал ранее в скайпе, есть проблема с WebDriverWait(wd, 1).until(EC.presence_of_element_located(( By.CSS_SELECTOR, "body"))), для ожидания полной загрузки страницы. Но был дан ответ, что это не обязательно. Добавил проверку ниже.
    WebDriverWait(wd, 30).until(EC.number_of_windows_to_be(2))
    wd.switch_to.window(new_window[0])
    wd.close()
    wd.switch_to.window(main_window)

wd.quit()