# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 22:17:51 2020

@author: Apoorva
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
search_url = "https://profootballtalk.nbcsports.com/category/rumor-mill/"



driver.get(search_url)
li=[]
divs = driver.find_elements_by_class_name('post-permalink')[:1]
res=[]
for i in divs:
    part=[]
   # driver.execute_script("document.getElementsByClassName('post-permalink').target='_blank'")
    driver.execute_script("window.open('');")
    k=i.get_attribute('href')
    driver.switch_to.window(driver.window_handles[1])
    driver.get(k)
    part.append(k)
    para=[x for x in driver.find_elements_by_tag_name('p') if(x.text!='')][0]
    photo_link=driver.find_elements_by_class_name('wp-post-image')[0].get_attribute('src')
    if('http' in photo_link or 'https'in photo_link):
        part.append(photo_link)
        part.append(para.text)
        res.append(part)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    #i.click()
    
    


   # i.click()
    
    
    




