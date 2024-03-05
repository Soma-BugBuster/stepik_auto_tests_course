import math
from selenium.webdriver.common.by import By
import time
from conftest import visible_chrome_driver


def test_alert(visible_chrome_driver):
    link = "http://suninjuly.github.io/alert_accept.html"
    visible_chrome_driver.get(link)
    try:
        input1 = visible_chrome_driver.find_element(By.CSS_SELECTOR, ".btn")
        input1.click()
        alert = visible_chrome_driver.switch_to.alert
        alert.accept()

        def calc(x):
            return str(math.log(abs(12 * math.sin(int(x)))))

        x_element = visible_chrome_driver.find_element(By.CSS_SELECTOR, "#input_value")
        x = x_element.text
        y = calc(x)
        input1 = visible_chrome_driver.find_element(By.CSS_SELECTOR, "#answer")
        input1.send_keys(y)
        button = visible_chrome_driver.find_element(By.CSS_SELECTOR, ".btn")
        button.click()

    finally:
        time.sleep(10)
