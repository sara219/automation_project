from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# => Setup The browser
driver = webdriver.Chrome()

baseUrl = "https://www.udemy.com/course/selenium-webdriver-and-python/"


try:
    driver.get(baseUrl)
    # print(driver.page_source)
    course_title_element = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "clp-lead__title"))
    )
    course_title = course_title_element.text
    print(course_title)

    # ! take to much time to load :(
    # section_titles = WebDriverWait(driver, 15).until(
    #     EC.visibility_of_all_elements_located(
    #         (By.CSS_SELECTOR, "span[class^='section--section-title--']")
    #     )
    # )

    # * write into the file
    with open("scraped_course.txt", "w") as file:
        file.write(course_title)
    print("✅ Saved to scraped_course.txt")

finally:
    driver.quit()
