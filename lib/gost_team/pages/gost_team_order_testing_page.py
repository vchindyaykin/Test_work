from selenium.webdriver.remote.webdriver import WebDriver

from lib.gost_team.elements.gost_team_order_testing_elements import GostTeamOrderTestingElements
from utils.page import Page


class GostTeamOrderTestingPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
        self.url = 'https://gost.team/orders'
        self.__driver = driver
        self.elems = GostTeamOrderTestingElements(driver=driver)

    def on_page(self):
        assert self.url == self.__driver.current_url
        self.attach_screenshot()

    def check_is_active_elements(self):
        elements = (
            self.elems.input_name_field,
            self.elems.input_email_field,
            self.elems.input_telegram_field,
        )
        for elem in elements:
            elem.is_enabled()
            elem.is_displayed()
