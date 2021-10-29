import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    # алерт
    # browser.execute_script('alert("Robots at work");')
    # замена титла документа
    # browser.execute_script('document.title="Script executing";')
    # все вместе
    browser.execute_script(
        'document.title="Скрипт выполняется"; '
        'alert("Robots at work");')
    # чтобы кликнуть на перекрытую кнопку, нам нужно выполнить следующие команды
    # button = browser.find_element(By.CSS_SELECTOR, "button")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # button.click()
    # Прокрутить страницу вниз на 100 пикселей
    # browser.execute_script("window.scrollBy(0, 100);")
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # ответ
