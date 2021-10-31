import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print('\nРаботает код фикстуры browser. Начало выполнения.')
    browser = webdriver.Chrome()
    print('browser запущен. Передается значение browser и управление тесту.')
    yield browser
    print('\nТест вернул управление фикстуре browser.')
    browser.quit()
    print('browser закрыт. Работа фикстуры browser завершена')


@pytest.fixture(scope='module', autouse=True)
def autorun():
    print('''
    Работает код фикстуры
    autorun(scope="module", autouse=True)
    в начале модуля''')
    yield
    print('''
    Работает код фикстуры
    autorun(scope="module", autouse=True)
    в конце модуля''')


class TestMainPage1:
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
