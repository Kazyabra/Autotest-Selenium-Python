"""
Если нужно проверить, что тест вызывает ожидаемое исключение ,
мы можем использовать специальную конструкцию
with pytest.raises().
Например, можно проверить, что на странице сайта не должен
отображаться какой-то элемент:
"""
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


"""
В первом тесте элемент будет найден, поэтому ошибка NoSuchElementException, 
которую ожидает контекстный менеджер pytest.raises, не возникнет, и тест упадёт.
"""
def test_exception1():
    browser = webdriver.Chrome()
    try:
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()


"""
Во втором тесте, как мы и ожидали, кнопка не будет найдена, и тест пройдет. 
"""
def test_exception2():
    browser = webdriver.Chrome()
    try:
        browser.get("http://selenium1py.pythonanywhere.com/")
        with pytest.raises(NoSuchElementException):
            browser.find_element(By.CSS_SELECTOR, "no_such_button.btn")
            pytest.fail("Не должно быть кнопки Отправить")
    finally:
        browser.quit()


if __name__ == "__main__":
    pytest.main()
