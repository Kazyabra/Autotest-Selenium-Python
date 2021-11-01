# запуск из консоли pytest -s -v -rx test_3_6_2_parametrize.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    print('Запуск браузера...')
    yield browser
    browser.quit()
    print('\nБраузер закрыт')


# тест запустится с каждыми из параметров: "ru", "en-gb"
@pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


# этот тест тоже запустится 3 раза
@pytest.mark.parametrize('run', ["первый запуск", "второй запуск", "третий запуск"])
def test_run(run):
    print(f'\n{run}')


if __name__ == '__main__':
    pytest.main()
