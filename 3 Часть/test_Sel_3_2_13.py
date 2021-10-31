import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestMyTrening(unittest.TestCase):

    def test_regonsite1(self, link="http://suninjuly.github.io/registration1.html"):
        # С ссылкой по умолчанию должен пройти тест
        browser = webdriver.Chrome()
        browser.get(link)
        try:
            # Ваш код, который заполняет обязательные поля
            inp = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.first')
            inp.send_keys('Ничоси!')
            inp = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.second')
            inp.send_keys('Ничоси!')
            inp = browser.find_element(By.CSS_SELECTOR, 'div.first_block input.third')
            inp.send_keys('Ничоси!')
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text
            # с помощью assertEqual проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual(welcome_text, 'Congratulations! You have successfully registered!',
                             'Что-то пошло не так, регистрация не завершена!')
        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(5)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_regonsite2(self):
        # С этой ссылкой должен спотыкаться на заполнении второго поля. Это правильно.
        link = "http://suninjuly.github.io/registration2.html"
        self.test_regonsite1(link)


if __name__ == "__main__":
    unittest.main()
    # ответ FAILED (errors=1)
