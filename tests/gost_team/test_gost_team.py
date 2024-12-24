import allure
import pytest
from lib.gost_team.pages.gost_team_order_testing_page import GostTeamOrderTestingPage
from lib.gost_team.pages.gost_team_page import GostTeamPage


@allure.feature('Тесты GostTeam')
class TestGostTeam:

    @pytest.fixture(scope='function', autouse=True)
    def setup(
        self,
        gost_team_page: GostTeamPage,
    ):
        self.page = gost_team_page

    @allure.story('Проверка возможности заказать тестирование')
    def test_order_testing(self):
        with allure.step('Открытие страницы'):
            self.page.open()
        with allure.step('Скриним элемент'):
            self.page.attach_screenshot_element(self.page.elems.header_xpath())
        with allure.step('Переход на страницу заказа'):
            order_page = self.page.go_to_ordering_testing_page()
        with allure.step('Проверяем что мы находимся на странице заказа'):
            order_page.on_page()
        with allure.step('Проверяем input\'ы'):
            order_page.check_is_active_elements()
