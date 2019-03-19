#element exist?
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

def is_element_present(driver, *args):
  try:
    driver.find_element(*args)
    return True
  except NoSuchElementException:
    return False

is_element_present(driver, By.name, "q")
###
def are_elements_present(driver, *args):
     return len(driver.find_elements(*args)) > 0

are_elements_present(driver, By.name, "q")
####################################################################

#wait element
 #настройка неявных ожиданий
driver.implicitly_wait(10)
element = driver.find_element_by_name("q")
 #явное ожидание появления элемента
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wait = WebDriverWait(driver, 10) # seconds
element = wait.until(EC.presence_of_element_located((By.NAME, "q")))
# обратите внимание, что локатор передается как tuple!
####################################################################

#find element by JS (Execute script) (nice wuth jquerry)
links = driver.execute_script("return $$('a:contains((WebDriver)')")
####################################################################

#send keys
from selenium.webdriver.common.keys import Keys
search_field.send_keys("selenium" + Keys.ENTER)

# если в поле есть маска -- надо перед вводом текста перейти в начало
date_field.send_keys(Keys.HOME + "01.01.2001")
####################################################################

#drag n drop
from selenium.webdriver.common.action_chains import ActionChains
ActionChains(driver).move_to_element(drag).click_and_hold().move_to_element(drop).release().perform()
####################################################################