# pytest -s -v --browser_name=firefox test_Sel_3_6_6.py
# или
# pytest -s -v --browser_name=chrome test_Sel_3_6_6.py
import pytest
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")


if __name__ == '__main__':
    pytest.main()
