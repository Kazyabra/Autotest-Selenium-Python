# pytest -s -v -rx Sel_3_6_3_ufo_find.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

otvet = '\n'


# @pytest.fixture(scope='module')
# def browser():
#     browser = webdriver.Chrome()
#     print('Запуск браузера...')
#     yield browser
#     browser.quit()
#     print('\nБраузер закрыт')


links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    global otvet
    # говорим WebDriver искать каждый элемент в течение 10 секунд
    browser.implicitly_wait(10)
    browser.get(link)
    # вычисляем ответ
    answer = str(math.log(int(time.time())))
    # отправляем ответ в поле и ждем когда кнопка станет кликабельна и
    # жмем на кнопку Отправить
    browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(answer)
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'button.submit-submission'))).click()
    # смотрим, что отвечает сайт
    feedback = browser.find_element(By.CSS_SELECTOR, 'pre.smart-hints__hint').text
    if feedback != 'Correct!':
        otvet = otvet + feedback
        print(otvet)
        # assert feedback == 'Correct!', feedback


if __name__ == '__main__':
    pytest.main()

# The owls are not what they seem! OvO
