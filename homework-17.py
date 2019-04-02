'''
Сделайте сценарий, который проверяет, не появляются ли в логе браузера сообщения при открытии страниц в учебном приложении, а именно -- страниц товаров в каталоге в административной панели.
Сценарий должен состоять из следующих частей:
1) зайти в админку
2) открыть каталог, категорию, которая содержит товары (страница http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1)
3) последовательно открывать страницы товаров и проверять, не появляются ли в логе браузера сообщения (любого уровня)
'''

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class MyListener(AbstractEventListener):
  def before_find(self, by, value, driver):
    print(by, value)
  def after_find(self, by, value, driver):
    print(by, value, "found")
  def on_exception(self, exception, driver):
    print(exception)

wd = EventFiringWebDriver(webdriver.Chrome(), MyListener())
wait = WebDriverWait(wd, 10) # seconds

wd.get('http://litecart.stqa.ru/admin/')
wd.find_element_by_name('username').send_keys('admin')
wd.find_element_by_name('password').send_keys('0b7dba1c77df25bf0')
wd.find_element_by_name('login').click()
wd.get("http://litecart.stqa.ru/admin/?app=catalog&doc=catalog&category_id=1&query=Duck")
elements = wd.find_elements_by_css_selector("td > a:not([title=Edit])")

ducks = []

for element in elements:
    ducks.append(element.text)

for duck in ducks:
    wd.find_element_by_link_text(duck).click()
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[name=save]")))
    for l in wd.get_log("browser"):
        print('Browser logs:', l)
    wd.back()

wd.quit()


