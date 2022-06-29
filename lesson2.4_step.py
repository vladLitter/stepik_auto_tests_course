from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

link = "http://suninjuly.github.io/redirect_accept.html"

try:

    browser.get(link)

    browser.find_element(By.CLASS_NAME, "trollface").click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value").text

    answer = calc(x)

    browser.find_element(By.ID, "answer").send_keys(answer)

    browser.find_element(By.CLASS_NAME, "btn").click()

finally:

    time.sleep(10)

    browser.quit()
