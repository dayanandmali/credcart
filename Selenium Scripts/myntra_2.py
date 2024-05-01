# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# driver = webdriver.Chrome()
# driver.get("https://www.myntra.com/")
# try:
#     search_bar = driver.find_element(By.XPATH,"//input[@placeholder='Search for products, brands and more']")
#     search_bar.send_keys("shirt")
#     search_bar.send_keys(Keys.RETURN)
#     WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//li[@class='product-base']")))
#     seventh_shirt = driver.find_element(By.XPATH,"//li[@class='product-base'][6]")
#     seventh_shirt.click()
#     size_button = driver.find_element(By.XPATH,"//p[@class='size-buttons-unified-size' and text()='42']")
#     size_button.click()
#     wishlist_button = driver.find_element(By.XPATH,"//a[@class='pdp-goToCart pdp-add-to-bag pdp-button pdp-flex pdp-center ']")
#     wishlist_button.click()
#     WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//span[@class='myntraweb-sprite desktop-iconBag sprites-headerBag']")))
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Navigate to the Myntra website
driver.get("https://www.myntra.com/")

try:
    # Find the search bar and enter "shirt"
    search_bar = driver.find_element(By.CSS_SELECTOR,"input[placeholder='Search for products, brands and more']")
    search_bar.send_keys("shirt")
    search_bar.send_keys(Keys.RETURN)  ## it will press the enter button

    # Wait for the search results to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-base")))

    # Click on the seventh shirt (index starts from 0)
    seventh_shirt = driver.find_element(By.XPATH,"//li[@class='product-base'][6]")
    time.sleep(3)
    seventh_shirt.click()

    # Select size 42 (you may need to adjust this based on the website structure)
    time.sleep(6)
    # size_button = driver.find_element(By.XPATH,"//p[text()='42']")
    size_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"body > div:nth-child(8) > div:nth-child(1) > div:nth-child(1) > main:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > button:nth-child(1) > p:nth-child(2)")))
    size_button.click()

    # Add to wishlist
    wishlist_button = driver.find_element(By.CSS_SELECTOR,".pdp-add-to-wishlist")
    wishlist_button.click()

    # Remove from cart
    cart_button = driver.find_element(By.CSS_SELECTOR,".pdp-remove-product")
    cart_button.click()

finally:
    # Close the browser
    driver.quit()
