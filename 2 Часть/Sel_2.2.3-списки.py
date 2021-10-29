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

link = "http://suninjuly.github.io/selects1.html"
link2 = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
try:
    # открываем сайт по ссылке
    browser.get(link2)

    # Берем x,y и вычисляем ответ
    element = browser.find_element(By.ID, 'num1')
    x = int(element.text)
    element = browser.find_element(By.ID, 'num2')
    y = int(element.text)
    otvet = x + y
    print(otvet, x, y)
    # кликаем список
    browser.find_element(By.ID, 'dropdown').click()
    # выбираем ответ
    otvet = f'option[value="{otvet}"]'
    print(otvet)
    browser.find_element(By.CSS_SELECTOR, otvet).click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # ответ
