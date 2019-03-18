'''
Сделайте сценарий, который проверяет, что при клике на товар открывается правильная страница товара в учебном приложении litecart.

Более точно, нужно открыть главную страницу, выбрать первый товар в блоке Campaigns и проверить следующее:

а) на главной странице и на странице товара совпадает текст названия товара
б) на главной странице и на странице товара совпадают цены (обычная и акционная)
в) обычная цена зачёркнутая и серая (можно считать, что "серый" цвет это такой, у которого в RGBa представлении одинаковые значения для каналов R, G и B)
г) акционная жирная и красная (можно считать, что "красный" цвет это такой, у которого в RGBa представлении каналы G и B имеют нулевые значения)
(цвета надо проверить на каждой странице независимо, при этом цвета на разных страницах могут не совпадать)
д) акционная цена крупнее, чем обычная (это тоже надо проверить на каждой странице независимо)

Необходимо убедиться, что тесты работают в разных браузерах, желательно проверить во всех трёх ключевых браузерах (Chrome, Firefox, IE).
'''
import sys

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_a():
    wd = webdriver.Chrome()
    wait = WebDriverWait(wd, 3) # seconds
    wd.get("http://litecart.stqa.ru/en/")

    #get product
    product = wd.find_element_by_css_selector("div#box-campaigns li.product a.link")
    index_name = product.find_element_by_css_selector("div.name").text
    product.click()
    sub_name = wd.find_element_by_css_selector("h1").text
    wd.quit()
    assert index_name == sub_name

def test_b():
    wd = webdriver.Chrome()
    wait = WebDriverWait(wd, 3) # seconds
    wd.get("http://litecart.stqa.ru/en/")

    product = wd.find_element_by_css_selector("div#box-campaigns li.product a.link")
    index_regulat_price = product.find_element_by_css_selector("s.regular-price").text
    index_sale_price = product.find_element_by_css_selector("strong.campaign-price").text
    product.click()
    sub_regular_price = wd.find_element_by_css_selector("s.regular-price").text
    sub_sale_price = wd.find_element_by_css_selector("strong.campaign-price").text
    assert index_regulat_price == sub_regular_price
    assert index_sale_price == sub_sale_price
    wd.quit()

