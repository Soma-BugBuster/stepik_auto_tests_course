import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Chrome_Options
from selenium.webdriver.firefox.options import Options as FF_Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: '--browser_name=chrome' or '--browser_name=firefox'")

    parser.addoption('--language', action='store', default=None,
                     help="Choose language: '--language=en', '--language=ru' or '--language=es'")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    if browser_name == "chrome":
        chrome_options = Chrome_Options()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("--disable-cache")
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        firefox_options = FF_Options()
        firefox_options.add_argument("--start-maximized")
        firefox_options.add_argument("--disable-cache")
        firefox_options.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    browser.implicitly_wait(20)
    yield browser
    browser.quit()

