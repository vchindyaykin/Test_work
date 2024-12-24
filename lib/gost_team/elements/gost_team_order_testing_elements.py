from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class GostTeamOrderTestingElements:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @property
    def input_email_field(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//input[@name="e-mail"]',
        )

    @property
    def input_name_field(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//input[@name="Имя"]',
        )

    @property
    def input_telegram_field(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//input[@name="Telegram"]',
        )
