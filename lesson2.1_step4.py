import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input_1 = browser.find_element(By.ID, "answer")
    input_1.send_keys(y)

    check_box_rob = browser.find_element(By.ID, "robotCheckbox")
    check_box_rob.click()

    radio_butt_rob = browser.find_element(By.ID, "robotsRule")
    radio_butt_rob.click()

    submit = browser.find_element(By.CLASS_NAME, "btn")
    submit.click()

finally:

    time.sleep(5)

    browser.quit()