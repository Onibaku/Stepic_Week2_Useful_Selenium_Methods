import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element_by_css_selector("#book.btn.btn-primary")
    button.click()

    x_element = browser.find_element_by_css_selector("#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer:required.form-control")
    answer.send_keys(y)

    button = browser.find_element_by_css_selector("#solve.btn.btn-primary")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
