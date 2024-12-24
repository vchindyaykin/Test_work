from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils.page import Page


class OkkoPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_okko(self):
        url = "https://okko.tv"
        self.open_site(url)
        self.attach_screenshot()
        return True

    def find_element_in_dom_tree(self, xpath=None):
        self.open_okko()
        self.xpath_is_present(xpath=xpath, silent = True)

    def find_element_in_search(self, xpath=None):
        self.xpath_is_present(xpath=xpath, silent = True)

    def okko_page_element_is_clickable(self, xpath=None):
        self.open_okko()
        self.element_is_clickable_xpath(xpath=xpath)
        self.refresh()

    def okko_page_click_to_element(self, xpath=None):
        self.open_okko()
        self.click_element(xpath=xpath)

    def click_and_proceed(self, xpath=None, expected_xpath=None):
        self.open_okko()
        self.click_to_proceed(xpath=xpath, expected_xpath=expected_xpath)

    def search_window(self, xpath=None, expected_xpath=None):
        self.open_okko()
        self.click_to_proceed(xpath=xpath, expected_xpath=expected_xpath)

    def fild(self, xpath=None, value=None):
        self.fild_search_window(xpath=xpath, value=value)
        self.click_element(xpath=xpath)

    def click_enter_button(self, xpath=None):
        self.emulate_click_enter_button(xpath=xpath)




