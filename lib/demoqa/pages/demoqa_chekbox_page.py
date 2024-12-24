from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from lib.demoqa.elements.demoqa_chekbox_page_elements import DemoQaCheckBoxElements
from utils.page import Page


class DemoQaCheckBoxPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
        self.url = 'https://demoqa.com/checkbox'
        self.__driver = driver
        self.elems = DemoQaCheckBoxElements(driver=driver)

    def open(self):
        self.open_site(
            url=self.url,
        )
        self.check_url_contains('checkbox')

    def is_button_state_changed(self):
        try:
            # Ожидание, пока иконка станет видимой
            WebDriverWait(self.elems.open_icon, 10).until(
                EC.visibility_of(self.elems.open_icon)
            )
            self.logger.info("Иконка стала видимой.")

            # Получение атрибута 'class' элемента
            class_attribute = self.elems.open_icon.get_attribute("class")
            self.logger.info(f"Атрибут class элемента: {class_attribute}")

            # Проверка, что класс содержит только 'rct-icon-parent-open'
            classes = class_attribute.split()  # Разделяем строку на отдельные классы
            if len(classes) == 1 and classes[0] == "rct-icon-parent-open":
                self.logger.info("Иконка содержит только нужный класс.")
                return True
            else:
                self.logger.info("Иконка содержит другие классы или не содержит нужного.")
                return False
        except Exception as e:
            self.logger.error(f"Ошибка при проверке состояния иконки: {e}")
            return False

    def is_visible_dropdown_elements(self):
        self.element_is_visible(self.elems.desktop_button)
        self.element_is_visible(self.elems.documents_button)
        self.element_is_visible(self.elems.downloads_button)

    def is_button_plus_changed_list(self):
        try:
            # Ожидание, пока иконка станет видимой
            WebDriverWait(self.elems.open_closed_list, 5).until(
                EC.visibility_of(self.elems.open_closed_list)
            )
            self.logger.info("Кнопка стала видимой.")

            # Получение атрибута 'class' элемента
            class_attribute = self.elems.open_closed_list.get_attribute("class")
            self.logger.info(f"Атрибут class элемента: {class_attribute}")

            # Проверка, что класс содержит только 'rct-node-expanded'
            classes = class_attribute.split()  # Разделяем строку на отдельные классы
            if "rct-node-expanded" in classes:
                self.logger.info("Кнопка содержит только нужный класс.")
                return True
            else:
                self.logger.info("Кнопка содержит другие классы или не содержит нужного.")
                return False
        except Exception as e:
            self.logger.error(f"Ошибка при проверке состояния Кнопки: {e}")
            return False

    def is_button_minus_changed_list(self):
        try:
            # Ожидание, пока иконка станет видимой
            WebDriverWait(self.elems.open_closed_list, 5).until(
                EC.visibility_of(self.elems.open_closed_list)
            )
            self.logger.info("Кнопка стала видимой.")

            # Получение атрибута 'class' элемента
            class_attribute = self.elems.open_closed_list.get_attribute("class")
            self.logger.info(f"Атрибут class элемента: {class_attribute}")

            # Проверка, что класс содержит только 'rct-node-collapsed'
            classes = class_attribute.split()  # Разделяем строку на отдельные классы
            if "rct-node-collapsed" in classes:
                self.logger.info("Кнопка содержит только нужный класс.")
                return True
            else:
                self.logger.info("Кнопка содержит другие классы или не содержит нужного.")
                return False
        except Exception as e:
            self.logger.error(f"Ошибка при проверке состояния Кнопки: {e}")
            return False