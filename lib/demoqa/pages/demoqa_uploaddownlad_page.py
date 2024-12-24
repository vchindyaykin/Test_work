from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import os
from lib.demoqa.elements.demoqa_uploaddownlad_page_elements import DemoQaUploadDownloadElements
from utils.page import Page


class DemoQaUploadDownloadPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
        self.url = 'https://demoqa.com/upload-download'
        self.__driver = driver
        self.elems = DemoQaUploadDownloadElements(driver=driver)

    def open(self):
        self.open_site(
            url=self.url,
        )
        self.check_url_contains('upload-download')

    def is_file_downloaded(self, download_folder: str, file_name: str) -> bool:
        try:
            # Создание полного пути к файлу
            downloaded_file = os.path.join(download_folder, file_name)

            # Проверка наличия файла
            if os.path.exists(downloaded_file):
                self.logger.info(f"Файл '{file_name}' успешно скачан в {download_folder}")
                return True
            else:
                self.logger.error(f"Файл '{file_name}' не был найден в папке {download_folder}")
                return False
        except Exception as e:
            self.logger.error(f"Ошибка при проверке скачивания файла: {e}")
            return False

    def upload_file_and_check(self, file_path: str) -> bool:
        try:
            # Отправка пути к файлу в поле
            file_input = self.__driver.find_element(By.XPATH, '//*[@id="uploadFile"]')
            file_input.send_keys(file_path)
            self.logger.info(f"Файл '{file_path}' успешно загружен.")
        except Exception as e:
            self.logger.error(f"Ошибка при загрузке файла: {e}")
            return False

    def check_uploaded_file(self, expected_value: str):
        # Находим элемент
        element = self.__driver.find_element(By.XPATH, '//*[@id="uploadedFilePath"]')
        # Получаем текст элемента
        file_path = element.text
        # Проверяем, что текст совпадает с ожидаемым значением
        if file_path == expected_value:
            self.logger.info(f"Строка '{expected_value}' отображается.")
        else:
            self.logger.error(f"Строка не совпадает. Ожидалось '{expected_value}'")
