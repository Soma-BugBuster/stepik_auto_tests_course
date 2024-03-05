from section4.pages.locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_empty_basket()

    def should_be_empty_basket(self):
        actual = self.check_element_text(*BasketPageLocators.BASKET_EMPTY_TEXT)
        expected = "Your basket is empty. Continue shopping"
        self.compare_elements_text(expected, actual)
        assert self.is_not_element_present(*BasketPageLocators.ITEM_IN_BASKET), \
            "Item(s) in the Basket are presented, but should not be"
