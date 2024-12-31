from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Chrome()
try:
    driver.get("https://www.javatpoint.com/")
    time.sleep(5)
    check_element=driver.find_element(By.TAG_NAME,"h1")
    if check_element.text.strip()=="Discover Your Journey with Us":
        searchTextBox=driver.find_element(By.NAME,"search")
        searchTextBox.send_keys("tags in html")
        time.sleep(5)
        searchTextBox.send_keys(Keys.ENTER)
        time.sleep(5)
        print("Passed")
finally:
    driver.quit()