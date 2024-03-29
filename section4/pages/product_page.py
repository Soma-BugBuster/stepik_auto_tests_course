from time import sleep

from .base_page import BasePage
from .locators import ProductPageLocators

"""
Описать в нем метод для добавления в корзину.
Дописать методы-проверки. Ожидаемый результат: 
1) Сообщение о том, что товар добавлен в корзину (получаем локатор > текст в элементе). 
2) Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили 
(получаем название товара на 1 странице, сравниваем со второй).
3) Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара (цену берём на 1 странице). 
"""


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_a_checkout()
        self.should_not_be_success_message()
        self.should_not_be_success_message_after_adding_product_to_basket()
        self.should_be_disappeared_success_message()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_a_checkout(self):
        precheck_product_name = self.check_element_text(*ProductPageLocators.PRECHECK_PRODUCT_NAME)
        precheck_product_price = self.check_element_text(*ProductPageLocators.PRECHECK_PRICE)
        self.click_to_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        self.solve_quiz_and_get_code()
        checkout_product_name = self.check_element_text(*ProductPageLocators.CHECKOUT_PRODUCT_NAME)
        checkout_product_price = self.check_element_text(*ProductPageLocators.CHECKOUT_PRICE)
        self.compare_elements_text(precheck_product_name, checkout_product_name)
        print("Название продукта корректно.")
        self.compare_elements_text(precheck_product_price, checkout_product_price)
        print("Цена корректна.")

    def should_not_be_success_message_after_adding_product_to_basket(self):
        self.click_to_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        self.solve_quiz_and_get_code()
        # sleep(60)
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        self.click_to_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        self.solve_quiz_and_get_code()
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should be"
