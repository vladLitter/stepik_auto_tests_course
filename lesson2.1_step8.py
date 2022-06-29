from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:

    browser.get(link)

    input_1 = browser.find_element(By.NAME, "firstname").send_keys("Vlad")

    input_2 = browser.find_element(By.NAME, "lastname").send_keys("Saga")

    input_3 = browser.find_element(By.NAME, "email").send_keys("saagavladislav@gmail.com")

    attach = browser.find_element(By.ID, "file")

    current_dir = os.path.abspath(os.path.dirname(__file__))

    file_path = os.path.join(current_dir, "file.txt")

    attach.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, "btn").click()

finally:

    time.sleep(10)

    browser.quit()
