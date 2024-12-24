import time
from os import times

from selenium.webdriver.remote.webdriver import WebDriver

from lib.gost_team.pages.gost_team_order_testing_page import GostTeamOrderTestingPage
from utils.page import Page
from lib.gost_team.elements.elements import GostTeamElements


class GostTeamPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
        self.url = 'https://gost.team/'
        self.__driver = driver
        self.elems = GostTeamElements(driver=driver)

    def open(self):
        self.open_site(
            url=self.url,
        )
        self.element_is_visible(self.elems.header())
        self.check_url_contains('gost.team')
        self.attach_screenshot()

    def go_to_ordering_testing_page(self) -> GostTeamOrderTestingPage:
        self.elems.order_testing_button().is_displayed()
        self.elems.order_testing_button().is_enabled()
        self.elems.order_testing_button().click()
        return GostTeamOrderTestingPage(driver=self.__driver)
