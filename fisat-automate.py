from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome()
try:
    driver.get("https://fisat.ac.in/")
    time.sleep(5)
    Academics=driver.find_element(By.ID,"menu-item-dropdown-4054")
    Academics.click()
    time.sleep(3)
    Departments=driver.find_element(By.ID,"menu-item-dropdown-4059")
    Departments.click()
    time.sleep(3)
    ca=driver.find_element(By.ID,"menu-item-dropdown-4144")
    ca.click()
    time.sleep(3)
    expectedTitle="Computer Applications | FISAT | Federal Institute of Science And Technology"
    actualTitle=driver.title
    if actualTitle==expectedTitle:
        print("Passed")
    else:
        print("Failed")
finally:
    driver.quit()