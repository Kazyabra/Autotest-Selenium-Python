# команда на запуск из консоли (запустится только промаркированный как smoke тест)
# pytest -s -v -m smoke test_fixture8.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    print('\nbrowser запущен. Передается значение browser и управление тесту.')
    yield browser
    browser.quit()
    print('\nbrowser закрыт. Работа фикстуры browser завершена')


class TestMainPage1:

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

if __name__ == '__main__':
    pytest.main()

