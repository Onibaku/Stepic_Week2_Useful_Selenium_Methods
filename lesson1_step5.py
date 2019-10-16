import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer:required.form-control")
    answer.send_keys(y)

    option1 = browser.find_element_by_css_selector("#robotCheckbox.form-check-input")
    option1.click()

    option2 = browser.find_element_by_css_selector('[value="robots"].form-check-input')
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
