import time
import pytest
import allure
from conftest import browser
from lib.okko.fixturies import okko_web_page
from lib.okko.okko_page import OkkoPage
from lib.okko.elements import Elements


class TestOkkoPage:
    @pytest.fixture(autouse=True, scope='function')
    def setup(self, okko_web_page: OkkoPage):
        self.page = okko_web_page  # Устанавливаем значение в фикстуре
        self.element = Elements
