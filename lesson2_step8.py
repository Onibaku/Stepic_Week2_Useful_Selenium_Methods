import os
import time
from selenium import webdriver

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('input:required[name="firstname"].form-control')
    input1.send_keys("123")

    input2 = browser.find_element_by_css_selector('input:required[name="lastname"].form-control')
    input2.send_keys("123")

    input3 = browser.find_element_by_css_selector('input:required[name="email"].form-control')
    input3.send_keys("123")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'somefile.txt')
    send_file = browser.find_element_by_css_selector('input:required[type="file"]')
    send_file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
