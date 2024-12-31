from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome()
try:
    driver.get("https://www.amazon.com/")
    time.sleep(5)
    searchTextBox=driver.find_element(By.ID,"twotabsearchtextbox")
    searchTextBox.send_keys("iphone16")
    time.sleep(25)
    searchTextBox.send_keys(Keys.ENTER)
    time.sleep(5)
    print("Passed")
finally:
    driver.quit()