import allure
import pytest
from lib.demoqa.pages.demoqa_uploaddownlad_page import DemoQaUploadDownloadPage
import time


@allure.feature('Тестирование UI DemoQa checkbox')
class TestDemoQaPageCheckbox:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, demoqa_page_upload_download: DemoQaUploadDownloadPage):
        self.page = demoqa_page_upload_download  # Устанавливаем значение в фикстуре

    @allure.story('Открытие страницы')
    def test_open_main_page(self):
        with allure.step('Открытие страницы'):
            self.page.open()
        with allure.step('Делаем скриншот'):
            self.page.attach_screenshot()

    @allure.story('Проверка скачивания файла')
    def test_download_file(self):
        with allure.step('Открытие страницы'):
            self.page.open()
            time.sleep(2)
        with allure.step('Проверка отображения кнопки скачивания'):
            self.page.element_is_visible(self.page.elems.download_button)
        with allure.step('Клик по кнопке "Download"'):
            self.page.click_element_by_xpath(self.page.elems.download_button)
            time.sleep(3)
        with allure.step('Проверка скаченного файла'):
            self.page.is_file_downloaded('C:\\Users\\GT00020\\Downloads', 'sampleFile.jpeg')
        with allure.step('Делаем скриншот'):
            self.page.attach_screenshot()

    @allure.story('Проверка загрузки файла')
    def test_upload_file(self):
        with allure.step('Открытие страницы'):
            self.page.open()
            time.sleep(2)
        with allure.step('Проверка отображения кнопки загрузки'):
            self.page.element_is_visible(self.page.elems.upload_button)
        with allure.step('Загрузка файла'):
            self.page.upload_file_and_check('C:\\Users\\GT00020\PycharmProjects\\rabotaem\\test_img\\sampleFile.jpeg')
        with allure.step('Проверка отображения строки с файлом'):
            self.page.element_is_visible(self.page.elems.string_upload_file)
        with allure.step('Проверка отображения названия файла в строке'):
            self.page.check_uploaded_file('C:\\fakepath\sampleFile.jpeg')
