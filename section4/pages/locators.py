from selenium.webdriver.common.by import By


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group > [href='/en-gb/basket/']")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    SIGN_UP_FORM = (By.CSS_SELECTOR, "#register_form")
    SIGN_UP_EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    SIGN_UP_PASSWORD_FIELD = (By.CSS_SELECTOR, "#register_form > div:nth-of-type(2) .form-control")
    SIGN_UP_CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "div:nth-of-type(3) .form-control")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-primary")
    PRECHECK_PRICE = (By.CSS_SELECTOR, ".price_color")
    PRECHECK_PRODUCT_NAME = (By.CSS_SELECTOR, "h1")
    CHECKOUT_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > "
                                       "p:nth-child(1) > strong")
    CHECKOUT_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div")


class BasketPageLocators:
    BASKET_EMPTY_TEXT = (By.CSS_SELECTOR, "p")
    ITEM_IN_BASKET = (By.CSS_SELECTOR, ".basket-items > .row")
