import random
import string

import pytest
import requests

from data import URL, ENDPOINT_GREATE_USER, ENDPOINT_CHANGE_AND_DELETE_USER_DATA
from helpers import generate_random_string


@pytest.fixture(scope="function")
def register_new_user_and_return_email_password():
    # создаём список, чтобы метод мог его вернуть
    email_pass = []

    # генерируем логин, пароль и имя курьера
    email = generate_random_string() + '@yandex.ru'
    password = generate_random_string()
    name = generate_random_string()

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(f'{URL}{ENDPOINT_GREATE_USER}', data=payload)

    email_pass.append(email)
    email_pass.append(password)
    email_pass.append(name)

    yield email_pass

    r = response.json()
    at = r['accessToken']

    requests.delete(f"{URL}{ENDPOINT_CHANGE_AND_DELETE_USER_DATA}", headers={
        'Authorization': at}, data=payload)


