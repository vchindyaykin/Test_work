from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class AvitoPageElements:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
    @property
    def button_search(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//button[@data-marker="search-form/submit-button"]',
        )
    @property
    def input_search(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//input[@data-marker="search-form/suggest/input"]',
        )
    @property
    def button_business(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//a[text()="Для бизнеса"]',
        )
    @property
    def button_category(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//button[@data-marker="top-rubricator/all-categories"]',
        )
    @property
    def button_cars(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//a[text()="Транспорт"]',
        )
    @property
    def button_jeep(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//a[@data-name="Вездеходы"]',
        )