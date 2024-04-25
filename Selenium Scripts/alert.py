import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# Information alert
driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
Alert(driver).accept()
print("succes message :",driver.find_element(By.XPATH,"//p[@id='result']").text)

driver.find_element(By.XPATH,"//button[@onclick='jsConfirm()']").click()
alert = Alert(driver)
alert.accept()
print(driver.find_element(By.XPATH,"//p[@id='result']").text)

driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()

alert=Alert(driver)
alert.send_keys("Hii,I am dayanand")
alert.accept()
print("jsPrompt message :",driver.find_element(By.XPATH,"//p[@id='result']").text)
time.sleep(4)