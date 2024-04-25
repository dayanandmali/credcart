from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
username = driver.find_element("xpath","//input[@placeholder='Username']")
username.send_keys("Admin")
pas = driver.find_element("xpath","//input[starts-with(@type,'pass')]")
pas.send_keys("admin123")
btn = driver.find_element("xpath","//button[@type='submit']")
btn.click()
acttitle = driver.title
exptitle = "OrangeHRM"

if exptitle==acttitle:
    print("Test case is pass...")
else:
    print("Test case is fail...")
time.sleep(3)

admin = driver.find_element("xpath","//li[1]//a[1]//span[1]")
print(admin.text)
admin.click()

name = driver.find_element("xpath","//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/input")
select = driver.find_element("xpath","//i[@class='oxd-icon bi-caret-up-fill oxd-select-text--arrow']").click()
admin=driver.find_element("xpath","")

time.sleep(5)