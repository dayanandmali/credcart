import time

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()
print("Title of the page :",driver.title)
print("URL of the page :",driver.current_url)

driver.get("https://www.amazon.com/")
print("title of the page :",driver.title)
print("current URl of the page :",driver.current_url)

driver.back()
time.sleep(3)
driver.forward() 

driver.get("https://www.gmail.com/")
driver.minimize_window()
title = driver.title
url = driver.current_url
print("title 0f the page :",title)
print("URL of the page :",url)
driver.close()
# driver.quit()