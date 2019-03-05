from selenium import webdriver

wd = webdriver.Chrome()
wd.get('https://google.com')
wd.__exit__()