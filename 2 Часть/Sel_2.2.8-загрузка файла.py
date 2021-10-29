import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
try:
    # открываем сайт по ссылке
    browser.get(link)

    # получаем путь к директории текущего исполняемого файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла
    file_path = os.path.join(current_dir, 'testfile.html')
    # ищем кнопку загрузки файла
    file_button = browser.find_element(By.ID, 'file')
    # загружаем наш файл
    file_button.send_keys(file_path)

    # заполняем поля
    element1 = browser.find_element(By.NAME, 'firstname')
    element2 = browser.find_element(By.NAME, 'lastname')
    element3 = browser.find_element(By.NAME, 'email')
    element1.send_keys('Ничоси!')
    element2.send_keys('Ничоси!')
    element3.send_keys('Ничоси!')


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # ответ 28.915072905148147
