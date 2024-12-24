import allure
import pytest
from lib.avito.avito_page import AvitoPage
from lib.avito.fixtures import avito_web_page


@allure.feature('Тестирование UI Авито')
class TestAvitoPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, avito_web_page: AvitoPage):
        self.page = avito_web_page  # Устанавливаем значение в фикстуре

    @allure.story('Открытие страницы')
    def test_open_main_page(self):
        self.page.open_avito_check()
        self.page.attach_screenshot()

    def test_element_visible(self):
        self.page.avito_element_is_visible()

    def test_input(self):
        self.page.avito_send_keys_to_input()

    def test_is_click(self):
        self.page.avito_is_click()

    def test_click_button(self):
        self.page.avito_click_button()

    def test_search_function(self):
        self.page.avito_search_for_item()

    def test_transfer_business(self):
        self.page.avito_transfer_business()

    def test_avito_categoty(self):
        self.page.avito_category()
