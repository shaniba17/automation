from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome()
try:
    driver.get("https://www.flipkart.com/")
    time.sleep(5)
    searchTextBox=driver.find_element(By.NAME,"q")
    searchTextBox.send_keys("ipad")
    time.sleep(5)
    searchTextBox.send_keys(Keys.ENTER)
    time.sleep(5)
    print("Passed")
finally:
    driver.quit()