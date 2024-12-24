from selenium.webdriver.remote.webdriver import WebDriver
from utils.page import Page
from lib.avito.elements.avito_page_elements import AvitoPageElements


class AvitoPage(Page):
    def __init__(self, driver: WebDriver):
        super().__init__(driver=driver)
        self.__elements = AvitoPageElements(driver=driver)


    @property
    def elems(self):
        return self.__elements

    def open_avito(self):
        url = 'https://www.avito.ru/'
        self.open_site(url)
        return True

    def open_avito_check(self):
        """Открывает сайт Avito."""
        url = 'https://www.avito.ru/'
        self.open_site(url)
        return True

    def avito_element_is_visible(self):
        self.open_avito()
        self.element_is_visible(self.elems.button_search, timeout=0)

    def avito_send_keys_to_input(self):
        self.open_avito()
        self.send_keys_to_input(self.elems.input_search, 'Lexus GS 350', timeout=0)

    def avito_is_click(self):
        self.open_avito()
        self.element_is_clickable(self.elems.button_search, timeout=0)

    def avito_click_button(self):
        self.open_avito()
        self.click_element(self.elems.button_search, timeout=0)

    def avito_search_for_item(self):
        """Выполняет поиск товара на сайте Avito."""
        self.open_avito()
        self.send_keys_to_input(self.elems.input_search, 'Lexus GS 350', timeout=0)
        self.element_is_clickable(self.elems.button_search)
        self.click_element(self.elems.button_search)
        self.check_url_contains("q")

    def avito_transfer_business(self):
        """Выполняет переход на страницу бизнеса сайта Avito."""
        self.open_avito()
        self.element_is_clickable(self.elems.button_business)
        self.click_element(self.elems.button_business)
        self.check_url_contains("business")

    def avito_category(self):
        self.open_avito()
        self.element_is_clickable(self.elems.button_category)
        self.click_element(self.elems.button_category)
        self.click_element(self.elems.button_cars)
        self.element_is_clickable(self.elems.button_jeep)
        self.click_element(self.elems.button_jeep)
        self.check_url_contains("vezdehody")
