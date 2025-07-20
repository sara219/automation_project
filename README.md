# End-to-End Automation Testing

## Objective

**End-to-End automation testing for:**

- valid and invalid flow
- Logout functionality
- Verifying login success and error handling
- Scraping Udemy course title and headings

### File Structure

```bash
automation_project/
├── automation_script.py     # Main script
├── scraped_course.txt       # Output from scraping Udemy
└── README.md                # Instructions
```

---

## 🖇️ Test Cases

### 📎 TC001: Valid Login

| Field               | Value                                                                                |
| ------------------- | ------------------------------------------------------------------------------------ |
| **Test Case ID**    | TC\_001                                                                              |
| **Title**           | Successful login with valid credentials                                              |
| **Preconditions**   | User is on login page                                                                |
| **Test Steps**      | 1. Enter username = `student`<br>2. Enter password = `Password123`<br>3. Click Login |
| **Expected Result** | User sees message "Logged In Successfully" and Logout button                         |
| **Actual Result**   | "Logged In Successfully" Message and Logout button Appear!                           |
| **Status**          | Pass                                                                                 |

### 📎 TC002: Login with invalid username, valid password

| Field               | Value                                                                                |
| ------------------- | ------------------------------------------------------------------------------------ |
| **Test Case ID**    | TC\_002                                                                              |
| **Title**           | Login with invalid username, valid password                                          |
| **Preconditions**   | User is on login page                                                                |
| **Test Steps**      | 1. Enter username = `studt`<br>2. Enter password = `Password123`<br>3. Click Login   |
| **Expected Result** | Error message "Your username is invalid!" is displayed                               |
| **Actual Result**   | "Your username si invalid" Message Appear!                                           |
| **Status**          | Pass                                                                                 |

### 📎 TC003: Login with valid username, and invalid password

| Field               | Value                                                                                |
| ------------------- | ------------------------------------------------------------------------------------ |
| **Test Case ID**    | TC\_002                                                                              |
| **Title**           | Login with invalid username, valid password                                          |
| **Preconditions**   | User is on login page                                                                |
| **Test Steps**      | 1. Enter username = `student`<br>2. Enter password = `password1245`<br>3. Click Login   |
| **Expected Result** | Error message "Your username is invalid!" is displayed                               |
| **Actual Result**   | "Your username si invalid" Message Appear!                                           |
| **Status**          | Pass                                                                                 |
