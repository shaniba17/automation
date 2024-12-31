from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
try:
    driver.get("http://10.0.16.206:5501/test.html")
    time.sleep(5)
    usernameTextBox=driver.find_element(By.ID,"username")
    usernameTextBox.send_keys("admin")
    time.sleep(3)
    passwordTextBox=driver.find_element(By.ID,"password")
    passwordTextBox.send_keys("12345")
    time.sleep(3)
    buttonTextBox=driver.find_element(By.ID,"login_button")
    buttonTextBox.click()
    time.sleep(3)
    expectedTitle="Dashboard"
    actualTitle=driver.title
    if actualTitle==expectedTitle:
        print("Passed")
        time.sleep(3)
        driver.back()
        time.sleep(3)
        usernameTextBox=driver.find_element(By.ID,"username")
        usernameTextBox.send_keys("user")
        time.sleep(3)
        passwordTextBox=driver.find_element(By.ID,"password")
        passwordTextBox.send_keys("1234")
        time.sleep(3)
        buttonTextBox=driver.find_element(By.ID,"login_button")
        buttonTextBox.click()
        time.sleep(3)
    else:
        print("Failed")
        time.sleep(3)
finally:
    driver.quit()