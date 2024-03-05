import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_button__add_to_basket_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket")))
    assert button, "Button not found"

