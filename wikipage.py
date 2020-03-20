# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 09:38:07 2020

@author: Apoorva
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
search_url = 'https://en.wikipedia.org/wiki/'
search_word='christino ronaldo'.replace(' ','_')
driver.get(search_url)

card=driver.find_elements_by_class_name('vcard')[0]
photo=driver.find_elements_by_class_name('image')[0].get_attribute('src')
age=driver.find_elements_by_class_name('forceAgeToShow').text
org=driver.find_elements_by_class_name('org').text