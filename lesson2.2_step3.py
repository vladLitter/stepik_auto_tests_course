from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def calc(x, y):
    return str(x + y)


link = "http://suninjuly.github.io/selects2.html"

try:

    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text
    answer = calc(int(num1), int(num2))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(answer)

    browser.find_element(By.CLASS_NAME, "btn").click()

finally:

    time.sleep(5)

    browser.quit()
