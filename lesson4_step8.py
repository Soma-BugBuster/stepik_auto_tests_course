import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

text = "$100"
price = WebDriverWait(browser, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), text)
)
button = browser.find_element(By.CSS_SELECTOR, "#book")
button.click()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
input1.send_keys(y)
button2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#solve")))
browser.execute_script("arguments[0].scrollIntoView();", button2)

button2.click()

alert = browser.switch_to.alert
print(alert.text)
