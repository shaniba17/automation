from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
try:
    driver.get("file:///C:/Users/shani/Downloads/Telegram%20Desktop/Selenium%20Programs/Demo/sample.html")
    time.sleep(5)
    check_element=driver.find_element(By.TAG_NAME,"h3")
    if check_element.text.strip()=="Admission for 2023 Batch":
        nameTextBox=driver.find_element(By.NAME,"name")
        nameTextBox.send_keys("sona")
        time.sleep(3)
        ageTextBox=driver.find_element(By.NAME,"age")
        ageTextBox.send_keys("21")
        time.sleep(3)
        ageTextBox=driver.find_element(By.NAME,"batch")
        ageTextBox.send_keys("B")
        time.sleep(3)
        print("Passed")
    else:
        print("Failed")
finally:
    driver.quit()