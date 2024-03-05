import pytest
from section4.pages.basket_page import BasketPage
from section4.pages.login_page import LoginPage
from section4.pages.product_page import ProductPage
from section4.pages.variables import Links


urls = [pytest.param(f"{Links.product_base_link}?promo=offer{i}", marks=pytest.mark.xfail(i == 7, reason=''))
        for i in range(10)]


@pytest.mark.parametrize('link', urls)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_a_checkout()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Links.coders_promo_offer0)
    page.open()
    page.should_not_be_success_message_after_adding_product_to_basket()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, Links.coders_promo_offer0)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, Links.coders_promo_offer0)
    page.open()
    page.should_be_disappeared_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, Links.city_and_the_stars)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, Links.city_and_the_stars)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, Links.main_page)
    page.open()
    page.open_basket()
    basket = BasketPage(browser, ProductPage.return_url)
    basket.should_be_empty_basket()


@pytest.mark.signup
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, Links.main_page)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, Links.product_base_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, Links.coders_promo_offer0)
        page.open()
        page.should_be_a_checkout()
