import os
import time  ### Этот импорт мне очень нужен чтобы не фейлились некоторые тесты!
import allure
from selenium.common import InvalidSessionIdException, NoSuchElementException, ElementClickInterceptedException, \
    StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.logger import Logger
from PIL import Image


class Page:
    def __init__(self, driver: WebDriver):
        self.__driver = driver
        self.browser_timeout = 2
        self.logger = Logger().get_logger()

    def _wait_to_load(self, xpath: str) -> None:
        self.logger.info(f'Ожидание загрузки элемента по xpath: {xpath}')
        try:
            WebDriverWait(driver=self.__driver, timeout=3).until(
                EC.visibility_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f'Элемент {xpath} успешно загружен')
        except Exception as e:
            self.logger.error(f'Элемент {xpath} не загрузился: {e}')
            raise Exception(f'Элемент {xpath} не загрузился: {e}')

    def open_site(self, url: str, error_message=None) -> None:
        self.logger.info(f'Попытка открыть сайт: {url}')
        try:
            self.__driver.get(url)
            self.logger.info(f'Сайт {url} открылся')
        except InvalidSessionIdException as e:
            message = f"Потеряно соединение с браузером. Возможно браузер был закрыт или аварийно завершил работу\n{e}"
            self.logger.error(message)
            raise InvalidSessionIdException(message)
        except Exception as e:
            message = f"Не удалось открыть сайт {url}"
            self.logger.error(f"{error_message}\n{e}" or message)
            raise Exception(message)

    def xpath_is_present(self, xpath: str, silent: bool = True) -> None:
        self.logger.info(f'Попытка найти элемент по xpath: {xpath}')
        try:
            self.__driver.find_element(by=By.XPATH, value=xpath)
            self.logger.info(f'Элемент {xpath} успешно найден')
        except NoSuchElementException:
            self.logger.warning(f'Элемент {xpath} не найден')
            if not silent:
                raise NoSuchElementException(f'Xpath: {xpath} не найден')

    def click_element(self, xpath: str) -> None:
        self.logger.info(f'Попытка кликнуть по элементу по xpath: {xpath}')
        self._wait_to_load(xpath)  # Ожидаем загрузку элемента
        try:
            element = self.__driver.find_element(by=By.XPATH, value=xpath)
            # element.click()
            if element.click() is not False:
                self.logger.info(f'Клик по элементу {xpath} выполнен успешно')
        except (ElementClickInterceptedException, StaleElementReferenceException) as e:
            self.logger.error(f'Не удалось кликнуть по элементу {xpath}: {e}')
            raise Exception(f'Не удалось кликнуть по элементу {xpath}: {e}')
        except NoSuchElementException as e:
            self.logger.error(f'Элемент не найден по xpath {xpath}: {e}')
            raise Exception(f'Элемент не найден по xpath {xpath}: {e}')

    def element_by_xpath_is_clickable(self, xpath: str) -> None:
        self.logger.info(f'Проверка доступности клика по элементу по xpath: {xpath}')
        self._wait_to_load(xpath)  # Ожидаем загрузку элемента
        try:
            self.__driver.find_element(by=By.XPATH, value=xpath)
            is_clickable = EC.element_to_be_clickable((By.XPATH, xpath))(self.__driver)
            if is_clickable:
                self.logger.info(f'Элемент {xpath} доступен для клика')
            else:
                raise Exception(f'Элемент {xpath} не доступен для клика')
        except (NoSuchElementException, StaleElementReferenceException) as e:
            self.logger.error(f'Ошибка при проверке кликабельности элемента {xpath}: {e}')
            raise Exception(f'Ошибка при проверке кликабельности элемента {xpath}: {e}')

    def click_to_proceed(self, xpath: str, expected_xpath: str) -> None:
        self.logger.info(f'Проверка доступности клика по элементу по xpath: {xpath}')
        self._wait_to_load(xpath)  # Ожидаем загрузку элемента
        time.sleep(1)
        try:
            element = self.__driver.find_element(by=By.XPATH, value=xpath)
            WebDriverWait(self.__driver, 2).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element.click()
            self.logger.info(f'Кликнули по элементу {xpath}')
            time.sleep(1)
            # Ожидаем загрузку нового элемента
            WebDriverWait(self.__driver, 2).until(EC.presence_of_element_located((By.XPATH, expected_xpath)))
            time.sleep(1)
            self.logger.info(f'Элемент {expected_xpath} успешно загружен после клика по элементу {xpath}')
        except (NoSuchElementException, StaleElementReferenceException) as e:
            self.logger.error(f'Ошибка при попытке кликнуть по элементу {xpath}: {e}')
            raise Exception(f'Ошибка при попытке кликнуть по элементу {xpath}: {e}')

    def refresh(self):
        self.__driver.refresh()

    def element_is_visible(self, element: object, timeout: int = 2) -> bool:
        """
        Проверка, виден ли элемент на странице в течение заданного времени.
        """
        self.logger.info(f'Попытка проверить видимость элемента по xpath: {element}')
        try:
            WebDriverWait(self.__driver, timeout).until(
                EC.visibility_of(element)
            )
            self.logger.info(f'Элемент {element} видим на странице')
            return True
        except TimeoutException as e:
            self.logger.error(f'Элемент {element} не стал видимым за {timeout} секунд: {e}')
            return False
        except NoSuchElementException as e:
            self.logger.error(f'Элемент не найден по xpath {element}: {e}')
            return False

    def send_keys_to_input(self, element, text: str, timeout: int = 2) -> bool:
        """
        Отправка текста в поле ввода по xpath.
        """
        self.logger.info(f'Попытка отправить текст в поле ввода по xpath: {element}')
        try:
            input_field = WebDriverWait(self.__driver, timeout).until(
                EC.visibility_of(element)
            )
            input_field.clear()  # очищаем поле перед вводом
            input_field.send_keys(text)  # отправляем текст
            self.logger.info(f'Текст "{text}" успешно отправлен в поле {element}')
            return True
        except (TimeoutException, NoSuchElementException) as e:
            self.logger.error(f'Не удалось отправить текст в поле {element}: {e}')
            return False

    def click_element_by_xpath(self, element, timeout: int = 2) -> bool:
        """
        Кликает по элементу, если он видим и кликабелен.
        """
        self.logger.info(f'Попытка кликнуть по элементу: {element}')
        try:
            clickable_element = WebDriverWait(self.__driver, timeout).until(
                EC.element_to_be_clickable(element)
            )
            clickable_element.click()
            self.logger.info(f'Клик по элементу выполнен успешно')
            return True
        except TimeoutException:
            self.logger.error(f'Элемент не стал кликабельным за {timeout} секунд')
            return False
        except (ElementClickInterceptedException, StaleElementReferenceException) as e:
            self.logger.error(f'Ошибка при клике по элементу: {e}')
            return False

    def element_is_clickable(self, element, timeout: int = 2) -> bool:
        """
        Проверяет, доступен ли элемент для клика в течение заданного времени.
        """
        self.logger.info(f'Проверка кликабельности элемента: {element}')
        try:
            WebDriverWait(self.__driver, timeout).until(
                EC.element_to_be_clickable(element)
            )
            self.logger.info(f'Элемент {element} доступен для клика')
            return True
        except TimeoutException:
            self.logger.error(f'Элемент {element} не стал кликабельным за {timeout} секунд')
            return False
        except NoSuchElementException:
            self.logger.error(f'Элемент {element} не найден на странице')
            return False

    def element_is_clickable_xpath(self, xpath):
        """
        Проверяет, доступен ли элемент для клика в течение заданного времени.
        """
        self.logger.info(f'Проверка кликабельности элемента: {xpath}')
        self.__driver.find_element(by=By.XPATH, value=xpath)
        self._wait_to_load(xpath)  # Ожидаем загрузку элемента
        try:
            self.logger.info(f'Элемент {xpath} доступен для клика')
            return True
        except TimeoutException:
            self.logger.error(f'Элемент {xpath} не стал кликабельным за секунд')
            return False
        except NoSuchElementException:
            self.logger.error(f'Элемент {xpath} не найден на странице')
            return False

    def check_url_contains(self, substring: str, timeout: int = 2) -> bool:
        """Проверяет, содержит ли текущий URL указанный подстроку."""
        self.logger.info(f"Проверяем, что URL содержит подстроку: {substring}")
        try:
            WebDriverWait(self.__driver, timeout).until(
                lambda driver: substring in driver.current_url
            )
            self.logger.info(f"URL содержит подстроку: {substring}")
            return True
        except TimeoutException:
            self.logger.error(f"URL не содержит подстроку: {substring}")
            return False

    def fild_search_window(self, xpath, value):
        element = self.__driver.find_element(by=By.XPATH, value=xpath)
        element.send_keys(value)
        return value

    def emulate_click_enter_button(self, xpath):
        element = self.__driver.find_element(by=By.XPATH, value=xpath)
        time.sleep(1)
        element.send_keys(Keys.ENTER)
        self.logger.info(f"Эмулируем клик по кнопке ENTER внутри элемента")
        time.sleep(3)

    def attach_screenshot(self) -> None:
        """
        Аттачим скриншот к аллюру
        :return:
        """
        try:
            self.logger.info('Скриншотим и аттачим его к аллюру')
            allure.attach(
                self.__driver.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG,
            )
            self.logger.info('Скриншот успешно добавлен')
        except Exception:
            self.logger.info('Произошла ошибка при создании скриншота/его добавлении')

    def attach_screenshot_element(self, xpath: str) -> None:
        """
        Аттачим скриншот конкретного элемента по XPath к аллюру
        :param xpath: XPath элемента, который нужно заскриншотить
        :return: None
        """
        try:
            self.logger.info('Скриншотим элемент по XPath и аттачим его к аллюру')

            # Сначала делаем скриншот всей страницы
            self.__driver.save_screenshot("full_screenshot.png")

            # Находим элемент по XPath
            element = self.__driver.find_element(By.XPATH, xpath)

            # Получаем размеры и положение элемента
            location = element.location
            size = element.size

            # Открываем полное изображение и обрезаем его
            full_image = Image.open("full_screenshot.png")
            left = location['x']
            top = location['y']
            right = left + size['width']
            bottom = top + size['height']

            # Обрезаем изображение по координатам элемента
            element_image = full_image.crop((left, top, right, bottom))
            element_image.save("element_screenshot.png")

            # Аттачим скриншот элемента к Allure
            allure.attach.file("element_screenshot.png", name="Element Screenshot",
                               attachment_type=allure.attachment_type.PNG)

            self.logger.info('Скриншот элемента успешно добавлен')
        except Exception as e:
            self.logger.error(f'Произошла ошибка при создании скриншота/его добавлении: {e}')

        finally:
            # Удаляем файлы, если они существуют
            if os.path.exists("full_screenshot.png"):
                os.remove("full_screenshot.png")
                self.logger.info('Удален скриншот всей страницы (из папки с тестами, в атачах он остаётся)')

            if os.path.exists("element_screenshot.png"):
                os.remove("element_screenshot.png")
                self.logger.info('Удален скриншот элемента (из папки с тестами, в атачах он остаётся)')

    def find_element_by_xpath(self, xpath: str):
        """
        Поиск элемента на странице по XPATH
        :param xpath: str
        :return:
        """
        try:
            self.__driver.find_element(
                by=By.XPATH,
                value=xpath,
            )
            self.logger.info(f'Элемент найден')
        except NoSuchElementException:
            self.logger.error(f'Не удалось найти элемент по XPATH={xpath}')
            raise NoSuchElementException(f'Не удалось найти элемент по XPATH={xpath}')
