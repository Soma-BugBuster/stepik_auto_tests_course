import math
from selenium.common.exceptions import NoAlertPresentException, TimeoutException, NoSuchElementException
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import faker
from section4.pages.locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def switch_to_tab(self, tab_index):
        """
        Переключаемся на вкладку (выбираем по её индексу: tab_index).
        """
        self.browser.switch_to.window(self.browser.window_handles[tab_index])

    def check_full_url(self, expected_url):
        """
        Проверяем полное соответствие URL ожидаемому.
        """
        current_url = self.browser.current_url
        assert current_url == expected_url, f"Ошибка! Ожидался: {expected_url}. Фактический: {current_url}"

    def return_url(self):  # подумать, нужна ли эта функция или хватит check_full_url и check_part_of_url
        """
        :return: проверяем текущий урл
        """
        return self.browser.current_url

    def check_part_of_url(self, expected_url):
        """
        Проверяем соответствие части URL ожидаемому (для Terms of Use).
        """
        current_url = self.browser.current_url
        assert expected_url in current_url, f"Ошибка! Ожидался: {expected_url}. Фактический: {current_url}"

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    """
    Работаем с элементами страницы (включая поля ввода)
    """
    def wait_for_element(self, how, what, timeout=10):
        """
        Ожидаем появление элемента.
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((how, what))
        )

    def is_element_present(self, how, what):
        """
        :return: проверяем наличие элемента
        """
        try:
            self.wait_for_element(how, what)
            return True
        except NoSuchElementException:
            return False

    def is_not_element_present(self, how, what, timeout=4):
        """
        :return: проверяем отсутствие элемента
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        """
        :return: проверяем исчезание элемента
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def move_to_element(self, how, what):
        """
        :return: перемещаемся к элементу и наводим курсор
        """
        element_to_hover = self.wait_for_element(how, what)
        actions = ActionChains(self.browser)
        actions.move_to_element(element_to_hover).perform()

    def click_to_element(self, how, what):
        """
        Перемещаемся к элементу и кликаем на него.
        """
        selected_element = self.wait_for_element(how, what)
        actions = ActionChains(self.browser)
        actions.click(selected_element).perform()

    def open_basket(self):
        """
        Переходим в корзину по кнопке в шапке сайта.
        """
        self.click_to_element(*BasePageLocators.BASKET_BUTTON)

    def input_into_field(self, how, what, input_value):
        """
        Вводим данные в поле.
        Параметр input_value: можем задать конкретное значение.
        """
        selected_field = self.wait_for_element(how, what)
        selected_field.send_keys(input_value)

    @staticmethod
    def random_password(chars=10):
        """
        Генерирует рандомный пароль. Длина по умолчанию - 10. Принимаемые password() параметры:
        password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
        """
        password = faker.Faker().password(length=chars)
        return password

    @staticmethod
    def random_email():
        """
        Генерирует рандомный email.
        """
        email = faker.Faker().email()
        return email

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_element_text(self, how, what):
        selected_element = self.wait_for_element(how, what)
        element_text = selected_element.text
        return element_text

    @staticmethod
    def compare_elements_text(expected, actual):
        assert actual == expected, f"Ошибка! Ожидаемый текст: {expected}. Фактический текст: {actual}"
        return True

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    """
    Работаем с файлами (аттачи  и скриншоты)
    """

    def attach_file(self, how, what, file_path):
        """
        Прикрепляем файл.
        """
        selected_element = self.wait_for_element(how, what)
        self.browser.execute_script("arguments[0].scrollIntoView();", selected_element)
        selected_element.send_keys(os.path.abspath(file_path))

    def full_page_screenshot(self, file_name):
        """
        Делаем скриншот всей страницы (максимальные высоту и ширину вычисляем).
        """
        page_height = self.browser.execute_script(
            "return Math.max( document.body.scrollHeight, document.body.offsetHeight, "
            "document.documentElement.clientHeight, document.documentElement.scrollHeight, "
            "document.documentElement.offsetHeight );")

        window_width = self.browser.execute_script("return window.screen.width;")

        self.browser.set_window_size(window_width, page_height)
        self.browser.save_screenshot(file_name)
