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
import re

def funct (driver):
    wd = ''
    if driver == 'Chrome':
        wd = webdriver.Chrome()
    elif driver == 'Firefox':
        wd = webdriver.Firefox()
    else:
        return False
    wait = WebDriverWait(wd, 3) # seconds
    wd.get("http://litecart.stqa.ru/en/")

    product = wd.find_element_by_css_selector("div#box-campaigns li.product a.link")

    index_name = product.find_element_by_css_selector("div.name").text
    index_regular_price = product.find_element_by_css_selector("s.regular-price").text
    index_color_regular_price = product.find_element_by_css_selector("s.regular-price").value_of_css_property('color')
    index_fontsize_regular_price = product.find_element_by_css_selector("s.regular-price").value_of_css_property('font-size')

    index_sale_price = product.find_element_by_css_selector("strong.campaign-price").text
    index_color_sale_price = product.find_element_by_css_selector("strong.campaign-price").value_of_css_property('color')
    index_fontweight_sale_price = product.find_element_by_css_selector("strong.campaign-price").value_of_css_property('font-weight')
    index_fontsize_sale_price = product.find_element_by_css_selector("strong.campaign-price").value_of_css_property('font-size')

    product.click()

    sub_name = wd.find_element_by_css_selector("h1").text
    sub_regular_price = wd.find_element_by_css_selector("s.regular-price").text
    sub_color_regular_price = wd.find_element_by_css_selector("s.regular-price").value_of_css_property('color')
    sub_fontsize_regular_price = wd.find_element_by_css_selector("s.regular-price").value_of_css_property('font-size')

    sub_sale_price = wd.find_element_by_css_selector("strong.campaign-price").text
    sub_color_sale_price = wd.find_element_by_css_selector("strong.campaign-price").value_of_css_property('color')
    sub_fontweight_sale_price = wd.find_element_by_css_selector("strong.campaign-price").value_of_css_property('font-weight')
    sub_fontsize_sale_price = wd.find_element_by_css_selector("strong.campaign-price").value_of_css_property('font-size')

    wd.quit()

    #a
    if index_name == sub_name:
        print('name is equal')
    else:
        print('name not equal')
    #б
    if index_regular_price == sub_regular_price:
        print('regular price is equal')
    else:
        print('regular price not equal')

    if index_sale_price == sub_sale_price:
        print('sale price is equal')
    else:
        print('sale price not equal')
    #в
    regex = r"[0-9]{1,3}"
    matches = re.findall(regex, index_color_regular_price)
    r = matches[0]
    g = matches[1]
    b = matches[2]
    if r == g and r == b and g == b:
        print('index color is grey')
    else:
        print('index color is not is grey')

    matches = re.findall(regex, sub_color_regular_price)
    r = matches[0]
    g = matches[1]
    b = matches[2]
    if r == g and r == b and g == b:
        print('sub color is grey')
    else:
        print('sub color is not is grey')
    #г
    matches = re.findall(regex, index_color_sale_price)
    r = matches[0]
    g = matches[1]
    b = matches[2]
    if int(g) == 0 and int(b) == 0:
        print('index sale is red')
    else:
        print('index sale is not is red')

    matches = re.findall(regex, sub_color_sale_price)
    r = matches[0]
    g = matches[1]
    b = matches[2]
    if int(g) == 0 and int(b) == 0:
        print('sub sale is red')
    else:
        print('sub sale is not is red')

    if (int(index_fontweight_sale_price) >= 700):
        print("Index sale font is bold")
    else:
        print('Index not bold')

    if (int(sub_fontweight_sale_price) >= 700):
        print("Sub sale font is bold")
    else:
        print('Sub not bold')
    #д
    if float(index_fontsize_regular_price[:-2]) < float(index_fontsize_sale_price[:-2]):
        print('Index Sale font is bigger')
    else:
        print('Index Sale font not bigger')

    if float(sub_fontsize_regular_price[:-2]) < float(sub_fontsize_sale_price[:-2]):
        print('sub Sale font is bigger')
    else:
        print('sub Sale font not bigger')

funct('Chrome')
funct('Firefox')