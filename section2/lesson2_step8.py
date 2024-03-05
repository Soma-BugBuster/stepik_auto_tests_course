from selenium.webdriver.common.by import By
import time
import os
from conftest import visible_chrome_driver


def test_attach_file(visible_chrome_driver):
    try:
        link = "http://suninjuly.github.io/file_input.html"
        visible_chrome_driver.get(link)

        input1 = visible_chrome_driver.find_element(By.CSS_SELECTOR, "[name='firstname']")
        input1.send_keys("Ivan")
        input2 = visible_chrome_driver.find_element(By.CSS_SELECTOR, "[name='lastname']")
        input2.send_keys("Petrov")
        input3 = visible_chrome_driver.find_element(By.CSS_SELECTOR, "[name='email']")
        input3.send_keys("test@gmail.com")

        # choose_file_button = visible_chrome_driver.find_element(By.CSS_SELECTOR, "#file")

        attach = visible_chrome_driver.find_element(By.CSS_SELECTOR, "#file")
        current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого
        # файла
        file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
        attach.send_keys(file_path)

        button = visible_chrome_driver.find_element(By.CSS_SELECTOR, ".btn")
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        visible_chrome_driver.quit()
