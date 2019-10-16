import math
import time
from selenium import webdriver

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element_by_css_selector("button.btn.btn-primary")
    button1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_css_selector("#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer:required.form-control")
    answer.send_keys(y)

    button2 = browser.find_element_by_css_selector("button.btn")
    button2.click()

finally:
    time.sleep(15)
    browser.quit()
