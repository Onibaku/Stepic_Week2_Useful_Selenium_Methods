import time
from selenium import webdriver

link ="http://suninjuly.github.io/wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    button = browser.find_element_by_css_selector("button.btn.btn-primary")
    button.click()

    message = browser.find_element_by_id("verify_message")
    assert "successful" in message.text

finally:
    time.sleep(15)
    browser.quit()
