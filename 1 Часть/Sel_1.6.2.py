import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# ссылка на сайт
link = 'http://suninjuly.github.io/find_link_text'
# данные для ввода
values = [
    'Ivan',
    'Petrov',
    'Smolensk',
    'Russia'
]
# список полей ввода
inputs = [0]
# запускаем вебдравер хром
browser = webdriver.Chrome()
# пробуем
try:
    # открываем окно хрома по ссылке
    browser.get(link)
    # зашифрованная ссылка
    text = str(math.ceil(math.pow(math.pi, math.e)*10000))
    print(text)
    # переходим по зашифрованной ссылке
    link = browser.find_element(By.LINK_TEXT, text)
    link.click()
    # ищем поля по селектору и заполняем данными из values
    for number in range(1, len(values)+1):
        inputs.append(browser.find_element(By.CSS_SELECTOR, f'.form-group:nth-child({number}) input'))
        inputs[number].send_keys(values[number-1])
        print(f'{number} поле: {values[number-1]}')

    # ищем кнопку submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    # нажимаем кнопку submit
    submit_button.click()
finally:
    # пауза
    time.sleep(60)
    # закрываем все процессы драйвера
    browser.quit()
# ответ)) 25.20412293657999

