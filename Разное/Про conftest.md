# conftest.py
Для хранения часто употребимых фикстур и хранения глобальных настроек нужно использовать 
файл *conftest.py*, который должен лежать в директории верхнего уровня в вашем проекте с тестами. 
Можно создавать дополнительные файлы *conftest.py* в других директориях, но тогда настройки 
в этих файлах будут применяться только к тестам в под-директориях.

Теперь, сколько бы файлов с тестами мы ни создали, у тестов будет доступ к фикстурам в *conftest.py*. 
Фикстура передается в тестовый метод в качестве аргумента. Таким образом можно удобно 
переиспользовать одни и те же вспомогательные функции в разных частях проекта.

Если вы в параметрах укажете строки с кириллицей, например, 
*@pytest.mark.parametrize('string', ['вариант1', 'вариант2'])*, 
то она не отобразится корректно в списке запускаемых тестов в консоли.  
Чтобы это исправить нужно в файл **conftest.py** добавить строку:

    def pytest_make_parametrize_id(config, val): return repr(val)

## Conftest.py и передача параметров в командной строке
В conftest.py удобно будет будет добавить обработчик параметров командной строки для запуска тестов.  
Например выбор вебдрайвера хром или фаерфокс.  
Для запроса значения параметра мы можем вызвать команду:

    browser_name = request.config.getoption("browser_name")

Добавим логику обработки командной строки в conftest.py:

    import pytest
    from selenium import webdriver
    
    def pytest_addoption(parser):
        parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
        # Можно задать значение параметра по умолчанию, 
        # чтобы в командной строке не обязательно было указывать параметр --browser_name, например, так:
        # parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")

    @pytest.fixture(scope="function")
    def browser(request):
        browser_name = request.config.getoption("browser_name")
        browser = None
        if browser_name == "chrome":
            print("\nstart chrome browser for test..")
            browser = webdriver.Chrome()
        elif browser_name == "firefox":
            print("\nstart firefox browser for test..")
            browser = webdriver.Firefox()
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
        yield browser
        print("\nquit browser..")
        browser.quit()

## Пример нашего файла с тестом *test_parser.py*:

    link = "http://selenium1py.pythonanywhere.com/"

    
    def test_guest_should_see_login_link(browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

Запустим тесты на Firefox:

    pytest -s -v --browser_name=firefox test_parser.py

Запустим тесты на Chrome:

    pytest -s -v --browser_name=chrome test_parser.py
