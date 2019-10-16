import time
from selenium import webdriver

link ="http://suninjuly.github.io/cats.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    browser.find_element_by_id("button")
    #button.click()

finally:
    time.sleep(15)
    browser.quit()
