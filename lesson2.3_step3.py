from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

link = "http://suninjuly.github.io/execute_script.html"

try:

    browser.get(link)
    num = browser.find_element(By.ID, "input_value").text
    answer = calc(num)

    input_answer = browser.find_element(By.ID, "answer")

    browser.execute_script('return arguments[0].scrollIntoView(true);', input_answer)

    input_answer.send_keys(answer)

    robo_check = browser.find_element(By.ID, "robotCheckbox").click()

    robo_butt = browser.find_element(By.ID, "robotsRule").click()

    button = browser.find_element_by_tag_name("button").click()

finally:

    time.sleep(10)

    browser.quit()
