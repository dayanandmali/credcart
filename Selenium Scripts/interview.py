import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.alert import Alert
# alert =Alert(driver)

driver = webdriver.Chrome()
driver.get("https://www.magicbricks.com/")
budget = driver.find_element(By.XPATH, "//div[@onclick='showBudgetDropDown(event, this);fireSearchBoxClickedGTM();']")
budget.click()
price = driver.find_element(By.XPATH,"//div[text()='₹30000'and @class='mb-search__min-max__item'and @data-actualindex='5'and @onclick='onclick']")
price.click()
search = driver.find_element(By.CLASS_NAME, "mb-search__btn")
search.click()
# (driver.find_element(By.XPATH,"//div[@class='filter__component__drop-down']//div[@class='filter-budget__fieldset__min-max min']//select[@class='filter-budget__select']"))
agents = driver.find_element(By.XPATH, "//a[text()='Top Agents']")
agents.click()
names = driver.find_elements(By.XPATH, "//div[@class='prefagent__headersec__name']")
# print(names.count())
index = 1
for name, index in names:
    print(name.text)
    index=index+1
    if index == 20:
        break
print("finish the program...")
