from Logins import stepik  # мои логины
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

link1 = "https://stepik.org/catalog?auth=login"
link2 = "https://stepik.org/lesson/187065/step/11?unit=161976"

browser = webdriver.Chrome()

try:
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(10)
    # логинимся
    print(stepik(browser))
    # открываем урок по ссылке
    sleep(5)
    browser.get(link2)
    for count in range(10):
        # кликаем кнопку Рецензировать
        button_recense = browser.find_element(By.CSS_SELECTOR, 'button.is-outlined')
        sleep(5)
        button_recense.click()

        # кликаем радиокнопки
        sleep(1)
        button_radio = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "//section[1]//label[text()='1']")))
        button_radio.click()
        sleep(1)
        button_radio = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "//section[2]//label[text()='1']")))
        button_radio.click()
        sleep(1)
        button_radio = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "//section[3]//label[text()='1']")))
        button_radio.click()
        sleep(1)
        button_radio = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(
            (By.XPATH, "//section[4]//label[text()='1']")))
        button_radio.click()

        # заполняем поля
        inp = browser.find_element(By.XPATH,
                                   "//section[1]//textarea[@placeholder='Развернутое объяснение вашей оценки']")
        inp.send_keys('ссылка открывается')
        inp = browser.find_element(By.XPATH,
                                   "//section[2]//textarea[@placeholder='Развернутое объяснение вашей оценки']")
        inp.send_keys('описание есть')
        inp = browser.find_element(By.XPATH,
                                   "//section[3]//textarea[@placeholder='Развернутое объяснение вашей оценки']")
        inp.send_keys('задачи есть')
        inp = browser.find_element(By.XPATH,
                                   "//section[4]//textarea[@placeholder='Развернутое объяснение вашей оценки']")
        inp.send_keys('сообщение коммита осмыссленное')

        # заполняем итоговый камент
        # находим фрейм с редактором последнего коммента
        inp = browser.find_element(By.XPATH, "//section[5]//iframe")
        # переключаемся на этот фрейм
        browser.switch_to.frame(inp)
        # находим поле ввода
        inp = browser.find_element(By.XPATH, '//p')
        inp.send_keys('все ок')
        # переключаемся назад в фрейм по умолчанию
        browser.switch_to.default_content()

        # кликаем кнопку Отправить рецензию
        button_recense = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        sleep(7)
        button_recense.click()

        # нажимаем ок на алерте
        button_yes = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Да']")))
        sleep(1)
        # button_yes = browser.find_element(By.XPATH, "//button[text()='Да']")
        button_yes.click()
        sleep(5)
        print(f'отправлено {count + 1} рецензий')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
