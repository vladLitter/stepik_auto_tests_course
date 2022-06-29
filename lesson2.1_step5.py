from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    element_id = browser.find_element(By.ID, "treasure")
    element_value = element_id.get_attribute("valuex")
    y = calc(element_value)

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(y)

    check_box_rob = browser.find_element(By.ID, "robotCheckbox")
    check_box_rob.click()

    radio_butt_rob = browser.find_element(By.ID, "robotsRule")
    radio_butt_rob.click()

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()

finally:

    time.sleep(10)
    browser.quit()
