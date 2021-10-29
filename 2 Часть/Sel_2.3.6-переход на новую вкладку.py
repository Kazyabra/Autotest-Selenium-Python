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


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
try:
    # открываем сайт по ссылке
    browser.get(link)

    # жмем кнопку
    button = browser.find_element(By.CSS_SELECTOR, 'button')
    button.click()

    # переключаемся на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Берем х и вычисляем ответ
    x_element = browser.find_element(By.ID, 'input_value').text
    # Пишем ответ
    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(x_element))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # переключаемся на алерт
    alert = browser.switch_to.alert
    # получаем текст алерта и печатаем его в консоль
    otvet = alert.text.rsplit(maxsplit=1)
    otvet = otvet[1]
    print(f'Ответ: {otvet}')
    # жмем кнопку ОК
    alert.accept()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # ответ 28.958503206781586
