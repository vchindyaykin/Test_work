from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class DemoQaCheckBoxElements:
    def __init__(self, driver: WebDriver):
        self.__driver = driver

    @property
    def toggle_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="tree-node"]/ol/li/span/button'
        )

    @property
    def desktop_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//span[@class="rct-title" and text()="Desktop"]'
        )

    @property
    def documents_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//span[@class="rct-title" and text()="Documents"]'
        )

    @property
    def downloads_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//span[@class="rct-title" and text()="Downloads"]'
        )

    # Пока не делаю красиво xpath, а то с этой красотой потом ебаться часа 2, почему тесты не запускаются)
    @property
    def open_icon(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="tree-node"]/ol/li/span/label/span[2]/svg'
        )
    # Чисто для меня элемент
    @property
    def icon(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div/div[2]'
        )

    @property
    def plus_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="tree-node"]/div/button[1]'
        )

    @property
    def minus_button(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="tree-node"]/div/button[2]'
        )

    @property
    def open_closed_list(self):
        return self.__driver.find_element(
            by=By.XPATH,
            value='//*[@id="tree-node"]/ol/li'
        )