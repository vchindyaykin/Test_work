import allure
import pytest
from lib.demoqa.pages.demoqa_page import DemoQaPage
from lib.demoqa.elements.demoqa_elements import DemoQaElements


@allure.feature('Тестирование UI DemoQa')
class TestDemoQaPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, demoqa_page: DemoQaPage):
        self.page = demoqa_page  # Устанавливаем значение в фикстуре
        self.page.elems = DemoQaElements(self.page._DemoQaPage__driver)

    @allure.story('Открытие страницы')
    def test_open_main_page(self):
        with allure.step('Открытие страницы'):
            self.page.open()
        with allure.step('Делаем скриншот'):
            self.page.attach_screenshot_element(self.page.elems.header_xpath())

    def test_go_to_checkbox_page(self):
        with allure.step('Открытие страницы'):
            self.page.open()
        with allure.step('Переход к чекбоксу'):
            self.page.go_to_checkbox_page()

    def test_go_to_uploaddownload_page(self):
        with allure.step('Открытие страницы'):
            self.page.open()
        with allure.step('Переход к чекбоксу'):
            self.page.go_to_uploaddownload_page()
