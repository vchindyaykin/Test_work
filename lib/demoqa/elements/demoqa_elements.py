from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DemoQaElements:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @property
    def header(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value=str('//*[@id="app"]/header')
        )

    @property
    def element_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//div[@class="card-body"]/h5[text()="Elements"]'
        )

    @property
    def checkbox_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//li[span[text()="Check Box"]]'
        )

    @property
    def webtables_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value=f'//li[span[text()="Web Tables"]]'
        )

    @property
    def uploaddownload_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value=f'//li[span[text()="Upload and Download"]]'
        )

    @staticmethod
    def header_xpath():
        xpath = str('//*[@id="app"]/header')
        return xpath
