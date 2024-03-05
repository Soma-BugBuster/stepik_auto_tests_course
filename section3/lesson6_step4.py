import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('url', ["236895/step/1", "236896/step/1", "236897/step/1", "236898/step/1", "236899/step/1",
                                 "236903/step/1", "236904/step/1", "236905/step/1"])
class TestLogin:
    def test_login(self, browser, url):
        link = f"https://stepik.org/lesson/{url}/"
        browser.get(link)
        time.sleep(3)
        login_button = browser.find_element(By.CSS_SELECTOR, ".navbar__auth_login")
        login_button.click()
        email_field = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
        email_field.send_keys("elena.valieva.QA@gmail.com")
        pass_field = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
        pass_field.send_keys("$I22avPTx!AF6$hq&M2")
        enter_button = browser.find_element(By.CSS_SELECTOR, ".sign-form__btn")
        enter_button.click()
        time.sleep(5)
        answer = math.log(int(time.time()))
        field_for_answer = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")
        field_for_answer.send_keys(answer)
        time.sleep(2)
        send_button = browser.find_element(By.CSS_SELECTOR, ".submit-submission")
        send_button.click()
        time.sleep(2)
        feedback_expected = "Correct!"
        feedback_actual = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint")
        feedback_actual_text = feedback_actual.text
        assert feedback_actual_text == feedback_expected
