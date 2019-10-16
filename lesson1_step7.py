import math
import time
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_css_selector("img#treasure")
    treasure_value = treasure.get_attribute("valuex")
    print("value is: ", treasure_value)
    x = treasure_value
    y = calc(x)

    answer = browser.find_element_by_css_selector("#answer:required")
    answer.send_keys(y)

    option1 = browser.find_element_by_css_selector("#robotCheckbox.check-input")
    option1.click()

    option2 = browser.find_element_by_css_selector('[value="robots"].check-input')
    option2.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(15)
    browser.quit()
