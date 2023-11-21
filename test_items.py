import time
from selenium.webdriver.common.by import By


def test_check_add_to_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    assert add_to_basket_button.is_displayed(), "Кнопка 'Add to basket' не видна на странице"
    time.sleep(3)
