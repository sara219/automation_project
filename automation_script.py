from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# => Setup The browser
driver = webdriver.Chrome()

# ! Test Case 001: Valid Login:
try:
    print(" ➡ TC001: Testing Valid Login ...")
    # navigate to the login page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    sleep(1)

    # Enter VALID credentials
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "submit")

    username_input.send_keys("student")
    password_input.send_keys("Password123")
    login_btn.click()

    # success message:
    success_message = driver.find_element(By.CLASS_NAME, "post-title").text
    assert "logged in successfully" in success_message.lower()
    print("✅ MESSAGE FOUND!")

    # logout btn:
    logout_btn = driver.find_element(By.LINK_TEXT, "Log out")
    assert logout_btn.is_displayed()
    print("✅ LOGOUT BTN FOUND!")
    # TC001: Pass
    print("✅✅ Login Test Case 001: Passes")

except Exception as error:
    # TC001: Fail
    print("❌ Login Test Case 001: Failed", error)

# -------------------------------------------------
# ! Test Case 002: Login with invalid Username:
try:
    print(" ➡ TC002: Testing Login with Invalid Username...")
    # navigate to the login page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    sleep(5)

    # Enter INVALID credentials: wrong username
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "submit")

    username_input.send_keys("studt")
    password_input.send_keys("Password123")
    login_btn.click()

    # capture the error message
    error_msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )
    assert error_msg.is_displayed()
    print("⛔️ Error Message:", error_msg.text)

    assert "your username is invalid" in error_msg.text.lower()
    print("✅✅ Login Test Case 002: Passes")


except Exception as error:
    # TC002: Fail
    print("❌ Login Test Case 002: Failed", error)

# -------------------------------------------------
# ! Test Case 003: Login with invalid Password:
try:
    print("➡ TC003: Testing Login with Invalid Password...")

    # navigate to login page
    driver.get("https://practicetestautomation.com/practice-test-login/")
    sleep(1)

    # Enter VALID username, INVALID password
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_btn = driver.find_element(By.ID, "submit")

    username_input.send_keys("student")
    password_input.send_keys("password1245")
    login_btn.click()

    # Wait for error message
    err_msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )

    assert err_msg.is_displayed()
    print("⛔️ Error Message:", err_msg.text)

    # Updated assertion
    assert "your password is invalid" in err_msg.text.lower()
    print("✅✅ Login Test Case 003: Passes")

except Exception as error:
    print("❌ Login Test Case 003: Failed", error)