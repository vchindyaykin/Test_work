import json
import requests
from requests import Response
from utils import logger
import allure
from typing import Optional, Dict, Any
from utils.logger import Logger


# Настройка логирования
log = Logger().get_logger()

class Api:
    @staticmethod
    def get(url: str, params: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None):
        log.info(f"Отправка GET запроса к URL: {url} с параметрами: {params} и заголовком: {headers}")
        with allure.step(f"GET запрос к {url} с параметрами: {params} и заголовком: {headers}"):
            response = requests.get(url, params=params, headers=headers)
            log.info(f"Получен ответ: {response.status_code} с данными: {response.text}")  # Логируем ответ
            # Возвращаем статус-код и тело ответа
            try:
                data = response.json()  # Пытаемся декодировать ответ как JSON
                return {
                    'status_code': response.status_code,
                    'data': data,  # Здесь мы возвращаем данные, если они корректные
                    'headers': response.headers
                }
            except json.JSONDecodeError:
                # Если ответ не JSON, возвращаем текст как данные
                return {
                    'status_code': response.status_code,
                    'data': response.text  # Возвращаем текст ответа
                }

    @staticmethod
    def post(url: str, data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None):
        log.info(f"Отправка POST запроса к URL: {url} с данными: {data} и заголовком: {headers}")
        with allure.step(f"POST запрос к {url} с данными: {data} и заголовком: {headers}"):
            response = requests.post(url, json=data, headers=headers)
            log.info(f"Получен ответ: {response.status_code} с данными: {response.text}")  # Логируем ответ
            try:
                response_data = response.json()  # Пытаемся декодировать ответ как JSON
                return {
                    'status_code': response.status_code,
                    'data': response_data
                }
            except json.JSONDecodeError:
                return {
                    'status_code': response.status_code,
                    'data': response.text
                }

    @staticmethod
    def put(url: str, data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None):
        log.info(f"Попытка отправить PUT запрос к URL: {url} с данными: {data}")
        with allure.step(f"PUT запрос к {url} с данными: {data}"):
            response = requests.put(url, json=data, headers=headers)
            log.info(f"Получен ответ: {response.status_code} с данными: {response.text}")  # Логируем ответ
            try:
                response_data = response.json()  # Пытаемся декодировать ответ как JSON
                return {
                    'status_code': response.status_code,
                    'data': response_data
                }
            except json.JSONDecodeError:
                return {
                    'status_code': response.status_code,
                    'data': response.text
                }

    @staticmethod
    def delete(url: str, headers: Optional[Dict[str, str]] = None):
        log.info(f"Попытка отправить DELETE запрос к URL: {url}")
        with allure.step(f"DELETE запрос к {url}"):
            response = requests.delete(url, headers=headers)  # Передаем заголовки, если они есть
            log.info(f"Получен ответ: {response.status_code} с данными: {response.text}")  # Логируем ответ
            try:
                response_data = response.json()  # Пытаемся декодировать ответ как JSON
                return {
                    'status_code': response.status_code,
                    'data': response_data
                }
            except json.JSONDecodeError:
                return {
                    'status_code': response.status_code,
                    'data': response.text
                }

    @staticmethod
    def patch(url: str, data: Optional[Dict[str, Any]] = None, headers: Optional[Dict[str, str]] = None):
        log.info(f"Попытка отправить PATCH запрос к URL: {url} с данными: {data}")
        with allure.step(f"PATCH запрос к {url} с данными: {data}"):
            response = requests.patch(url, json=data, headers=headers)
            log.info(f"Получен ответ: {response.status_code} с данными: {response.text}")  # Логируем ответ
            try:
                response_data = response.json()  # Пытаемся декодировать ответ как JSON
                return {
                    'status_code': response.status_code,
                    'data': response_data
                }
            except json.JSONDecodeError:
                return {
                    'status_code': response.status_code,
                    'data': response.text
                }
