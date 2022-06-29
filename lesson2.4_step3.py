from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

link = "http://suninjuly.github.io/alert_accept.html"

try:

    browser.get(link)

    first_butt = browser.find_element(By.CLASS_NAME, "btn").click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element(By.ID, "input_value").text
    answer = calc(x)

    input_answer = browser.find_element(By.ID, "answer").send_keys(answer)

    last_butt = browser.find_element(By.CLASS_NAME, "btn").click()

finally:

    time.sleep(10)

    browser.quit()