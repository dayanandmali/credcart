
# "Python - Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
#  except the first char itself.
# Sample String : 'restartthecomputer'
# Expected Result: 'resta$thecompute$'""
import time

# Automate the following Flow in python with a framework you are comfortable -
    # 1. Launch chrome and navigate https://www.magicbricks.com/
# 2. Select Rent -> Budget -> above 30K
# 4. Print the Agent names of the 1st 20 search results

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("//www.magicbricks.com/")
# rent=driver.find_element(By.XPATH,"path").click()
# print(len(elements))
# for option in elements:
#     if option >=

# string = "restartthecomputer"
# findex = string.index("r",1,len(string))
# sindex = string.index("r",6,len(string))
# newstr=list(string)
# # print(newstr)
# newstr[findex]="$"
# newstr[sindex]="$"
# newstr="".join(newstr)
# # string=newstr
# print("my old string is : {}\nmy new string is : {}".format(string,newstr))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# driver = webdriver.Chrome()
# driver.get("https://www.magicbricks.com/")
# time.sleep(3)
# search = driver.find_element(By.XPATH,"//div[@class='mb-search__btn']")
# search.click()
# budget = driver.find_element(By.XPATH,"//div[@class='title-ellipsis'][normalize-space()='Budget']")
# budget.click()
# minamount = driver.find_element(By.XPATH,"//div[@class='filter__component__drop-down']//div[@class='filter-budget__fieldset__min-max min']//select[@class='filter-budget__select']")
# select = Select(minamount)
# select.select_by_value("35000")
# btn = driver.find_element("xpath","//a[normalize-space()='Top Agents']").click()
#
# agents = driver.find_element(By.CLASS_NAME," srp-agcrd__intobox--name")
# print(len(agents))











