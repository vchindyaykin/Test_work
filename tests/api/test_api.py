import pytest
import allure
from utils.base_api import Api


class TestAPI:
    base_url = "https://restful-booker.herokuapp.com"

    @pytest.fixture(autouse=True)
    def setup(self):
        """Создание бронирования перед выполнением тестов."""
        self.token = self.get_token()  # Получаем токен
        self.booking_id = None
        self.create_booking()

    def get_token(self):
        """Получение токена аутентификации."""
        auth_url = f"{self.base_url}/auth"  # Замените на правильный URL для получения токена
        credentials = {
            "username": "admin",  # Укажите ваше имя пользователя
            "password": "password123"  # Укажите ваш пароль
        }

        response = Api.post(auth_url, credentials)
        assert response['status_code'] == 200, f"Ожидался статус 200, но получен {response['status_code']}"
        return response['data']['token']  # Убедитесь, что ключ 'token' соответствует вашему ответу

    def create_booking(self):
        """Создание нового бронирования и сохранение ID."""
        booking_data = {
            "firstname": "Test",
            "lastname": "User",
            "totalprice": 123,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2024-01-01",
                "checkout": "2024-01-07"
            },
            "additionalneeds": "Breakfast"
        }

        booking_url = f"{self.base_url}/booking"
        response = Api.post(booking_url, booking_data, headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}"  # Используем токен
        })

        assert response['status_code'] == 200, f"Ожидался статус 200, но получен {response['status_code']}"
        self.booking_id = response['data']['bookingid']

    @allure.title('Тест: Проверка работоспособности API')
    @allure.step('Проверка пинга API')
    def test_ping_api(self):
        """Тест для проверки работоспособности API."""
        url = f"{self.base_url}/ping"

        # Выполнение GET запроса к эндпоинту ping
        response = Api.get(url)

        with allure.step('Проверка статуса ответа'):
            assert response['status_code'] == 201, f"Ожидался статус 201, но получен {response['status_code']}"

        with allure.step('Проверка тела ответа'):
            # Проверяем, что данные содержат 'Created'
            assert response['data'] == "Created", f"Ожидался ответ 'Created', но получен '{response['data']}'"

    @allure.title('Тест: Получение списка ID бронирований')
    @allure.step('Проверка возможности получения списка ID бронирований')
    def test_get_booking_ids(self):
        """Проверка возможности получения списка всех бронирований."""
        booking_ids_url = f"{self.base_url}/booking"

        response = Api.get(booking_ids_url)

        with allure.step('Проверка формата ответа'):
            assert response['status_code'] == 200, f"Ожидался статус 200, но получен {response['status_code']}"
            assert isinstance(response['data'], list), "Ответ должен быть списком бронирований"

    @allure.title('Тест: Получение конкретного бронирования')
    @allure.step('Проверка возможности получения конкретного бронирования')
    def test_get_booking(self):
        """Проверка возможности получения конкретного бронирования."""
        booking_url = f"{self.base_url}/booking/{self.booking_id}"

        response = Api.get(booking_url, headers={
            "Authorization": f"Bearer {self.token}"  # Используем токен
        })

        with allure.step('Проверка статуса ответа'):
            assert response['status_code'] == 200, f"Ожидался статус 200, но получен {response['status_code']}"

        with allure.step('Проверка наличия данных бронирования'):
            response_data = response['data']
            assert 'firstname' in response_data, "Имя отсутствует в ответе"
            assert 'lastname' in response_data, "Фамилия отсутствует в ответе"

    @allure.title('Тест: Частичное обновление бронирования')
    @allure.step('Проверка возможности частичного обновления бронирования')
    def test_partial_update_booking(self):
        """Проверка возможности частичного обновления существующего бронирования."""
        # Данные для обновления
        partial_update_data = {
            "firstname": "James",
            "lastname": "Brown"
        }

        # Формируем URL для обновления
        update_url = f"{self.base_url}/booking/{self.booking_id}"

        # Заголовки запроса
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="  # Используем базовый токен
        }

        # Отправляем PATCH-запрос
        response = Api.patch(url=update_url, data=partial_update_data, headers=headers)

        # Проверка статуса ответа
        assert response['status_code'] == 200, f"Ожидался статус 200, но получен {response['status_code']}. Ответ: {response['data']}"

        # Проверка обновленных данных
        response_data = response['data']
        assert response_data['firstname'] == partial_update_data['firstname'], "Имя не обновилось"
        assert response_data['lastname'] == partial_update_data['lastname'], "Фамилия не обновилась"

        print("Тест прошел успешно: данные успешно обновлены.")

    @allure.title('Тест: Обновление бронирования')
    @allure.step('Проверка возможности обновления бронирования')
    def test_update_booking(self):
        """Проверка возможности обновления существующего бронирования."""
        update_data = {
            "firstname": "Updated",
            "lastname": "User",
            "totalprice": 456,
            "depositpaid": False,
            "bookingdates": {
                "checkin": "2025-01-02",
                "checkout": "2025-01-08"
            },
            "additionalneeds": "Dinner"
        }

        update_url = f"{self.base_url}/booking/{self.booking_id}"

        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="  # Используем базовый токен
        }

        response = Api.put(url=update_url, data=update_data, headers=headers)

        with allure.step('Проверка статуса ответа'):
            assert response['status_code'] == 200, f"Ожидался статус 200, но получен {response['status_code']}. Ответ: {response['data']}"

        with allure.step('Проверка обновленных данных'):
            response_data = response['data']
            assert response_data['firstname'] == update_data['firstname'], "Имя не обновилось"
            assert response_data['lastname'] == update_data['lastname'], "Фамилия не обновилась"

    @allure.title('Тест: Удаление бронирования')
    @allure.step('Проверка возможности удаления бронирования')
    def test_delete_booking(self):
        """Проверка возможности удаления бронирования."""
        delete_url = f"{self.base_url}/booking/{self.booking_id}"

        # Заголовок для аутентификации
        headers = {
            "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM=",  # Используем базовую аутентификацию
            "Content-Type": "application/json"
        }

        # Удаляем бронирование
        response = Api.delete(delete_url, headers=headers)

        with allure.step('Проверка статуса ответа'):
            assert response['status_code'] == 201, f"Ожидался статус 201, но получен {response['status_code']}"

        # Проверка, что бронирование действительно удалено
        get_response = Api.get(url=f"{self.base_url}/booking/{self.booking_id}")
        assert get_response['status_code'] == 404, f"Ожидался статус 404, но получен {get_response['status_code']}. Ответ: {get_response['data']}"
