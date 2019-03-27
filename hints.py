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


#wait element
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wait = WebDriverWait(driver, 10) # seconds
# обратите внимание, что локатор передается как tuple!
element = wait.until(EC.presence_of_element_located((By.NAME, "q")))
element2 = wait.until(lambda d: d.find_element_by_name("q"))
####################################################################

#refresh element
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wait = WebDriverWait(driver, 10) # seconds
driver.refresh()
wait.until(EC.staleness_of(element))
####################################################################


#wait visible
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10) # seconds
wait.until(EC.visibility_of(element))
####################################################################

#dismiss alerts
alert = driver.switch_to_alert()
alert_text = alert.text
alert.accept()
# либо alert.dismiss()
####################################################################

#new tabs
main_window = driver.current_window_handle
old_windows = driver.window_handles
link.click() # открывает новое окно
# ожидание появления нового окна,
# идентификатор которого отсутствует в списке oldWindows,
# остаётся в качестве самостоятельного упражнения
new_window = wait.until(there_is_window_other_than(old_windows))
driver.switch_to_window(new_window)
# ...
driver.close()
driver.switch_to_window(main_window)
####################################################################

#switch to frame
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))
driver.switch_to_default_content()
####################################################################

#some shit with windows
driver.set_window_size(800, 600)
driver.maximize_window()
####################################################################