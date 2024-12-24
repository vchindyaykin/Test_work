from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class GostTeamElements:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    def order_testing_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value=f'//*[contains(text(), "{"заказать тестирование".upper()}")]'
        )

    def header(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value=str('//*[@id="nav709249988"]')
        )

    @staticmethod
    def header_xpath():
        xpath = str('//*[@id="nav709249988"]')
        return xpath