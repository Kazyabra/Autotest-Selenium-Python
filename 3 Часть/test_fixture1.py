# ссылка на документацию pytest
# https://docs.pytest.org/en/latest/how-to/xunit_setup.html?highlight=teardown

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def setup_module():
    print('\nБлок запускается в начале всего модуля')


def teardown_module():
    print('\nБлок запускается в конце всего модуля')


"""
setup- и teardown- методы в классе с тестами будут выполняться
1 раз в начале всех тестов класса, 2й раз в конце всех тестов
"""


class TestMainPage1:

    @classmethod
    def setup_class(self):
        print("\nstart browser для пакета тестов..")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("\nquit browser для пакета тестов..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


"""
Классический способ работы с фикстурами — создание setup- и teardown-методов в файле с тестами
первый выполняется в начале каждого теста, второй в конце
"""


class TestMainPage2:

    def setup_method(self):
        print("\nstart browser для каждого теста..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("\nquit browser для каждого теста..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


if __name__ == "__main__":
    pytest.main()
