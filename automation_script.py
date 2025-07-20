from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# => Setup The browser 
driver = webdriver.Chrome()

print("START OF TESTING")

# Login Function: 
def login(username, password):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()

# Open Login Page
driver.get('https://practicetestautomation.com/practice-test-login/')

# * Test Case 001: Valid Login: 
print(" ➡ TC001: Testing Valid Login ...")