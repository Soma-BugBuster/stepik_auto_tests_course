from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
try:
    browser.get(link)
    first = browser.find_element(By.CSS_SELECTOR, "h2 > span:nth-of-type(2)")
    x = int(first.text)
    second = browser.find_element(By.CSS_SELECTOR, "span:nth-of-type(4)")
    y = int(second.text)
    z = x + y
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(x + y))

    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    time.sleep(5)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
