import allure
import pytest
from lib.demoqa.pages.demoqa_chekbox_page import DemoQaCheckBoxPage


@allure.feature('Тестирование UI DemoQa checkbox')
class TestDemoQaPageCheckbox:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, demoqa_page_checkbox: DemoQaCheckBoxPage):
        self.page = demoqa_page_checkbox  # Устанавливаем значение в фикстуре

    @allure.story('Открытие страницы')
    def test_open_main_page(self):
        with allure.step('Открытие страницы'):
            self.page.open()
        with allure.step('Делаем скриншот'):
            self.page.attach_screenshot()

    @allure.story('Проверка раскрывающегося списка')
    def test_dropdown_displays_elements(self):
        with allure.step('Открытие страницы'):
            self.page.open()
        with allure.step('Проверка отображения кнопки раскрывающегося списка'):
            self.page.element_is_visible(self.page.elems.toggle_button)
        with allure.step('Раскрываем список'):
            self.page.click_element_by_xpath(self.page.elems.toggle_button)
        with allure.step('Проверяем смену иконки'):
            self.page.is_button_state_changed()
        with allure.step('Проверка присутствия элементов в раскрывающемся списке'):
            self.page.is_visible_dropdown_elements()
        with allure.step('Делаем скриншот'):
            self.page.attach_screenshot()

    @allure.story('Проверка раскрытия всего списка')
    def test_dropdown_displays_full_elements(self):
        with allure.step('Открытие страницы'):
            self.page.open()
        with allure.step('Проверка отображения кнопки раскрывающей список'):
            self.page.element_is_visible(self.page.elems.plus_button)
        with allure.step('Раскрываем список'):
            self.page.click_element_by_xpath(self.page.elems.plus_button)
        with allure.step('Проверяем изменение класса в элементе HTML'):
            self.page.is_button_plus_changed_list()
        with allure.step('Проверка присутствия элементов в раскрывающемся списке'):
            self.page.is_visible_dropdown_elements()
        with allure.step('Проверка отображения кнопки закрывающей список'):
            self.page.element_is_visible(self.page.elems.minus_button)
        with allure.step('Закрываем список'):
            self.page.click_element_by_xpath(self.page.elems.minus_button)
        with allure.step('Проверяем изменение класса в элементе HTML'):
            self.page.is_button_minus_changed_list()
        with allure.step('Делаем скриншот'):
            self.page.attach_screenshot()

    #Этот тест чисто для меня, я его потом удалю, я с помощью него проверяю новые методы
    # @allure.story('Проверка раскрывающегося списка')
    # def test_dropdown_displays_elements(self):
    #     with allure.step('Открытие страницы'):
    #         self.page.open()
    #     with allure.step('Проверка отображения кнопки раскрывающегося списка'):
    #         self.page.element_is_visible(self.page.elems.plus_button)
    #     # with allure.step('Проверяем смену иконки'):
    #     #     self.page.is_button_plus_changed()