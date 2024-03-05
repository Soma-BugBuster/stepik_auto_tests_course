"""
Про Exceptions
Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.

Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM изменился,
то получим StaleElementReferenceException.

Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры), и реальный
пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element(By.ID, "button")
button.click()

