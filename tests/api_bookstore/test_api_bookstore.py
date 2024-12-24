import pytest
import allure
import json
from utils.base_api import Api


class TestBookStoreAPI:
    base_url = "https://demoqa.com/BookStore/v1/Books"  # Исправленный URL

    @allure.title('Тест: Проверка GET API')
    @allure.step("Отправляем GET запрос")
    def test_ping_api_with_no_parameters(self):
        """Тест для проверки работоспособности API."""
        url = self.base_url

        # Выполнение GET запроса к эндпоинту
        response = Api.get(url, None, {'accept': 'application/json'})

        # Проверка статуса ответа
        with allure.step('Проверка статуса ответа'):
            assert response['status_code'] == 200, f"Ожидался статус 200, но получен {response['status_code']}"

        # Получение и логирование тела ответа
        with allure.step('Получение тела ответа'):
            body = response['data']  # Парсим тело ответа как JSON
            body_pretty = json.dumps(body, indent=2, ensure_ascii=False)  # Красивый вывод JSON
            allure.attach(body_pretty, 'Тело ответа (JSON)', allure.attachment_type.JSON)
            print(body_pretty)

        # Проверка и логирование заголовков ответа
        with allure.step('Проверка заголовков ответа'):
            dict_header = response['headers']
            header_text = '\n'.join(f'{key}: {value}' for key, value in dict_header.items())
            allure.attach(header_text, 'Хэдер ответа', allure.attachment_type.TEXT)

            # Проверяем конкретный заголовок
            server_value = dict_header.get('Server', '')
            assert server_value == 'nginx/1.17.10 (Ubuntu)', (
                f"Ожидался сервер 'nginx/1.17.10 (Ubuntu)', но получен '{server_value}'")
            if header_text is not None:
                print('\nHeaders:\n')
                print(header_text)