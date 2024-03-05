"""Для того чтобы гарантировать закрытие, даже если произошла ошибка в предыдущих строках, проще всего использовать
конструкцию try,finally:"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

browser = webdriver.Chrome()

try:
    browser.get(link)
    button = browser.find_element(By.XPATH, "//button[.='Submit']")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    time.sleep(30)
    browser.quit()
