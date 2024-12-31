from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
try:
    driver.get("file:///C:/Users/shani/Downloads/Telegram%20Desktop/Selenium%20Programs/Demo/index.html")
    time.sleep(5)
    check_element=driver.find_element(By.TAG_NAME,"h1")
    if check_element.text.strip()=="FISAT":
        nameTextBox=driver.find_element(By.NAME,"fname")
        nameTextBox.send_keys("SHANU")
        time.sleep(5)
        print("Passed")
    else:
        print("Failed")
finally:
    driver.quit()