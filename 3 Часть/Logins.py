from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
# мои пароли
from kozapass import login_to


def stepik(driver):
    """
    :param driver: драйвер браузера
    :return: логинится на сайте stepik
    """
    browser = driver
    link1 = "https://stepik.org/catalog?auth=login"

    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
    # логинимся
    browser.get(link1)
    login = browser.find_element(By.CSS_SELECTOR, "input[name='login']")
    password = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
    login.send_keys(login_to('stepik.org')[0])
    password.send_keys(login_to('stepik.org')[1])

    button_login = WebDriverWait(browser, 5).until(
        ec.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    button_login.send_keys(Keys.ENTER)
    return 'Учетные данные введены'
