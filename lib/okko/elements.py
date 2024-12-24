from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from lib.okko.okko_page import OkkoPage


class Elements(OkkoPage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @staticmethod
    def subscription_button():
        # Сокращён и работает
        xpath = str('//div[@id="root"]//button')
        return xpath

    @staticmethod
    def header():
        xpath = str('//header[1]')
        return xpath

    @staticmethod
    def footer_after_proceed_subscription_button():
        xpath = str('//*[@id="root"]/div/div[2]')
        return xpath

    @staticmethod
    def search_button():
        # Сокращён и работает
        xpath = str('//*[@test-id="nav_search"]')
        return xpath

    @staticmethod
    def find_input_window():
        # Сокращён и работает
        xpath = str('//*[@test-id="nav_search_form"]//input')
        return xpath

    @staticmethod
    def find_after_click_find_button():
        # Сокращён и работает
        xpath = str('//*[@id="root"]//section//span[contains(text(), "Война")]')
        return xpath

    @staticmethod
    def find_movies_element():
        # Сокращён и работает
        xpath = str('//*[@id="root"]//article[2]//div[contains(., "Фильмы")]//button//span')
        return xpath

    @staticmethod
    def expected_movies_element():
        # Сокращён и работает
        xpath = str('//*[@id="root"]//h1[contains(text(), "Фильмы")]')
        return xpath