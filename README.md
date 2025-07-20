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

## Test Cases

| Field               | Value                                                                                |
| ------------------- | ------------------------------------------------------------------------------------ |
| **Test Case ID**    | TC\_001                                                                              |
| **Title**           | Successful login with valid credentials                                              |
| **Preconditions**   | User is on login page                                                                |
| **Test Steps**      | 1. Enter username = `student`<br>2. Enter password = `Password123`<br>3. Click Login |
| **Expected Result** | User sees message "Logged In Successfully" and Logout button                         |
| **Actual Result**   | "Logged In Successfully" Message and Logout button Appear!                           |
| **Status**          | Pass                                                                                 |
