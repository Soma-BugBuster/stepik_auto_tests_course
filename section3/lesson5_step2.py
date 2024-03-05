"""
Для выборочного запуска таких тестов в PyTest используется маркировка тестов или метки (marks). Для маркировки
теста нужно написать декоратор вида @pytest.mark.mark_name, где mark_name — произвольная строка.

Создайте файл pytest.ini в корневой директории вашего тестового проекта
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

"""
Для запуска тестов с разными метками можно использовать логическое ИЛИ. Запустим smoke и regression-тесты:
-s -v -m "smoke or regression" test_fixture8.py

чтобы пропустить тест, его отмечают в коде как @pytest.mark.skip
"""