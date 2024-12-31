from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
try:
    driver.get("https://uoc.ac.in/")
    time.sleep(5)
    Academics=driver.find_element(By.ID,"menu1251")
    Academics.click()
    time.sleep(3)
    Departments=driver.find_element(By.ID,"menu589")
    Departments.click()
    time.sleep(3)
    centers=driver.find_element(By.ID,"menu618")
    centers.click()
    time.sleep(3)
    itsr=driver.find_element(By.ID,"menu1214")
    itsr.click()
    time.sleep(3)
    expectedTitle="Home"
    actualTitle=driver.title
    if actualTitle==expectedTitle:
        print("Passed")
    else:
        print("Failed")
finally:
    driver.quit()