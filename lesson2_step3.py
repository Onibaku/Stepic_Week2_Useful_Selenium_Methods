import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector("#num1.nowrap").text

    num2 = browser.find_element_by_css_selector("#num2.nowrap").text

    result = str(int(num1) + int(num2))

    select = Select(browser.find_element_by_css_selector("#dropdown.custom-select"))
    select.select_by_value(result)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
