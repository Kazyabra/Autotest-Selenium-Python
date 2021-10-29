import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    """
    :param x: берем переменную с сайта
    :return: возвращаем значение, которое нужно ввести в текстовое поле
    """
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
try:
    # открываем сайт по ссылке
    browser.get(link)

    # Берем х и вычисляем ответ
    x_element = browser.find_element(By.ID, 'input_value')
    y = calc(x_element.text)
    print(y)
    # Пишем ответ
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)
    # выбираем и тычем в чекбокс
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    # проверяем какая радиокнопка выбрана
    radio_human = browser.find_element(By.ID, 'peopleRule')
    human_chk = radio_human.get_attribute('checked')
    assert human_chk is not None, 'Радиокнопка человека не выбрана по умолчанию'
    print(f'Значение атрибута checked радиокнопки человека: {human_chk}')

    # выбираем и тычем в радиокнопку
    radio_robot = browser.find_element(By.ID, 'robotsRule')
    radio_robot.click()
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # ответ 28.86724346263292
