from selenium.webdriver.remote.webdriver import WebDriver
from lib.demoqa.pages.demoqa_chekbox_page import DemoQaCheckBoxPage
from lib.demoqa.pages.demoqa_uploaddownlad_page import DemoQaUploadDownloadPage
from utils.page import Page
from lib.demoqa.elements.demoqa_elements import DemoQaElements


class DemoQaPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
        self._DemoQaPage__driver = driver
        self.url = 'https://demoqa.com/'
        self.__driver = driver
        self.elems = DemoQaElements(driver=driver)

    def open(self):
        self.open_site(
            url=self.url,
        )
        self.check_url_contains('demoqa')
        self.attach_screenshot()

    def go_to_checkbox_page(self) -> DemoQaCheckBoxPage:
        self.elems.element_button.click()
        self.elems.checkbox_button.click()
        self.check_url_contains('checkbox')
        self.attach_screenshot()
        return DemoQaCheckBoxPage(driver=self.__driver)

    def go_to_uploaddownload_page(self) -> DemoQaUploadDownloadPage:
        self.elems.element_button.click()
        self.elems.uploaddownload_button.click()
        self.check_url_contains('upload-download')
        self.attach_screenshot()
        return DemoQaUploadDownloadPage(driver=self.__driver)

