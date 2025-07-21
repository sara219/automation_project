# End-to-End Automation Testing
This project contains an end-to-end automation test suite using Selenium WebDriver in Python to validate the login workflow

**Test Target:**
<https://practicetestautomation.com/practice-test-login/>

**The test covers:**
- Valid login
- Invalid username login
- Invalid password login
- Access to a protected page directly
- Logout
- Bonus: Scraping course information from a Udemy course page

---

### Project Structure
```bash
automation_project/
├── automation_script.py     # Main script
├── scraped_course.txt       # Output from scraping Udemy
└── README.md                # Instructions
```

---

### Prerequisites
Ensure you have the following installed and configured:
- Python 3.7+
- Google Chrome Browser
- ChromeDriver
- Python packages
Install required packages using pip:
```bash
pip install selenium
```

---

How to Run
- Open a terminal or in the project directory.
- Run the login script:
```bash
python3 automation_script.py 
```
- The script will launch Chrome, run all test cases, print results in the console, and finally close the browser.
- Run the Scraping script:
```bash
python3 scaping_tc.py 
```
- Check the scraped_course.txt file.
---

## 🖇️ Test Cases

| **Test Case ID** | **Title**                        | **Preconditions**           | **Test Steps**                                                                                                                                             | **Expected Result**                                                       | **Status**                             |
| ---------------- | ------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | ------------------------------------ |
| **TC001**        | Login with Valid Credentials     | User is on Login Page       | 1. Enter username: `student`<br>2. Enter password: `Password123`<br>3. Click Login                                                                         | User is logged in successfully, sees success message and Logout button    | ✅ Pass                              |
| **TC002**        | Login with Invalid Username      | User is on Login Page       | 1. Enter username: `studt`<br>2. Enter password: `Password123`<br>3. Click Login                                                                           | Error message appears: "Your username is invalid!"                        | ✅ Pass                              |
| **TC003**        | Login with Invalid Password      | User is on Login Page       | 1. Enter username: `student`<br>2. Enter password: `password124`<br>3. Click Login                                                                         | Error message appears: "Your password is invalid!"                        | ✅ Pass                              |
| **TC004**        | Access "Protected" Page Directly | User is NOT Logged In       | 1. Navigate directly to: `/logged-in-successfully/`                                                                                                        | Page loads successfully (Note: not actually protected)                    | ✅ Pass (site not enforcing protection) |
| **TC005**        | Logout and Confirm Session Ended | User is Logged In           | 1. Login with valid credentials<br>2. Click "Log out"<br>3. Confirm redirect to login page                                                                 | User is redirected to login page after logout                             | ✅ Pass                              |
| **Bonus**        | Scrape Udemy Course Info         | Udemy Course URL Accessible | 1. Navigate to [Udemy Course Page](https://www.udemy.com/course/selenium-webdriver-and-python/)<br>2. Extract course title & headings<br>3. Save to `.txt` | Course title and section headings are saved in `udemy_course_content.txt` | ✅ Pass                              |
