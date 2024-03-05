"""На данной странице пауза перед появлением кнопки установлена на 1 секунду, метод find_element() сделает только
одну попытку найти элемент и в случае неудачи уронит наш тест.
"""


from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text
