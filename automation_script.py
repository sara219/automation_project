from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# => Setup The browser
driver = webdriver.Chrome()
baseUrl = "https://practicetestautomation.com/practice-test-login/"


# Get element function/ function helper:
def login_element(username, password):
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "submit").click()


# ! Test Case 001: Valid Login:
try:
    print(" ➡ TC001: Testing Valid Login ...")
    # navigate to the login page
    driver.get(baseUrl)

    # Enter VALID credentials
    login_element("student", "Password123")

    # success message:
    success_message = driver.find_element(By.CLASS_NAME, "post-title").text
    assert "logged in successfully" in success_message.lower()
    print("✅ MESSAGE FOUND!")

    # logout btn:
    logout_btn = driver.find_element(By.LINK_TEXT, "Log out")
    assert logout_btn.is_displayed()
    print("✅ LOGOUT BTN FOUND!")
    # TC001: Pass
    print("✅✅ TC001: Passes")

except Exception as error:
    # TC001: Fail
    print("❌ TC001: Failed", error)

# -------------------------------------------------
# ! Test Case 002: Login with invalid Username:
try:
    print(" ➡ TC002: Testing Login with Invalid Username...")
    # navigate to the login page
    driver.get(baseUrl)

    # Enter INVALID credentials: wrong username
    login_element("studt", "Password123")

    # capture the error message
    error_msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )
    assert error_msg.is_displayed()
    print("⛔️ Error Message:", error_msg.text)

    assert "your username is invalid" in error_msg.text.lower()
    print("✅✅ TC002: Passes")


except Exception as error:
    # TC002: Fail
    print("❌ TC002: Failed", error)

# -------------------------------------------------
# ! Test Case 003: Login with invalid Password:
try:
    print("➡ TC003: Testing Login with Invalid Password...")

    # navigate to login page
    driver.get(baseUrl)

    # Enter VALID username, INVALID password
    login_element("student", "password124")

    # Wait for error message
    err_msg = WebDriverWait(driver, 6).until(
        EC.visibility_of_element_located((By.ID, "error"))
    )
    assert err_msg.is_displayed()
    print("⛔️ Error Message:", err_msg.text)

    # Updated assertion
    assert "your password is invalid" in err_msg.text.lower()
    print("✅✅ TC003: Passed")

except Exception as error:
    print("❌ TC003: Failed", error)

# -------------------------------------------------
# ! Test Case 004: Access Protected Page:
try:
    print("➡ TC004: Access Protected Page (not actually protected) ...")

    driver.get("https://practicetestautomation.com/logged-in-successfully/")
    success_msg = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "post-title"))
    )
    assert "logged in successfully" in success_msg.text.lower()
    print("✅✅ TC004: Passed")

except Exception as error:
    print("❌ TC004: Failed", error)

# -------------------------------------------------
# ! Test Case 005: Logout:

try:
    print("➡ TC005: Logout and Session End ...")
    driver.get(baseUrl)

    # Enter VALID credentials
    login_element("student", "Password123")
    logout_btn = driver.find_element(By.LINK_TEXT, "Log out")
    assert logout_btn.is_displayed()
    print("✅ logout btn found!")

    # logout
    logout_btn.click()
    # Check redirection to login page
    current_url = driver.current_url
    assert "practice-test-login" in current_url.lower()

    # title = driver.find_element(By.TAG_NAME, "h1").text
    # assert "test login" in title.lower()
    print("✅✅ TC005: Passed")


except Exception as error:
    print("❌ TC005: Failed", error)

driver.quit()
print("Browser closed. Test completed.")
