from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DemoQaUploadDownloadElements:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @property
    def download_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="downloadButton"]'
        )

    @property
    def upload_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="uploadFile"]'
        )

    @property
    def string_upload_file(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="uploadedFilePath"]'
        )