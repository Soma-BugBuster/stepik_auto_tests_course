import pytest
from Stepik.Автоматизация_тестирования_с_помощью_Selenium_и_Python.section4.pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

urls = [pytest.param(f"{product_base_link}?promo=offer{i}", marks=pytest.mark.xfail(i == 7, reason='')) for i in
        range(10)]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_a_checkout()
