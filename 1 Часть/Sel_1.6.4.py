import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# ссылка на сайт
link = 'http://suninjuly.github.io/find_xpath_form'

# запускаем вебдравер хром
browser = webdriver.Chrome()
# пробуем
try:
    # открываем окно хрома по ссылке
    browser.get(link)
    # ищем поля по селектору и заполняем данными из values
    elements = browser.find_elements(By.CSS_SELECTOR, 'input')
    # заполняем поля
    for element in elements:
        element.send_keys('Ничоси!')
    # ищем кнопку submit
    submit_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    # нажимаем кнопку submit
    submit_button.click()
finally:
    # пауза
    time.sleep(60)
    # закрываем все процессы драйвера
    browser.quit()
# ответ

