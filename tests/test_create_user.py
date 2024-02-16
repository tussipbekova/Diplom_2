import allure
import pytest
import requests

from data import URL, ENDPOINT_GREATE_USER
from helpers import generate_random_string


@allure.title('Создание пользователя')
class TestCreateUser:

    name = generate_random_string()
    email = generate_random_string() + '@yandex.ru'
    password = generate_random_string()

    @allure.step('Успешное создание уникального пользователя')
    def test_create_unique_user(self):
        payload = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }

        response = requests.post(f"{URL}{ENDPOINT_GREATE_USER}", data=payload)

        r = response.json()
        s = r['success']

        assert response.status_code == 200 and s is True

    @allure.step('Неуспешное создание уже зарегистрированного пользователя')
    def test_create_registered_user(self):

        payload = {
            "email": self.email,
            "password": self.password,
            "name": self.name
        }

        response = requests.post(f"{URL}{ENDPOINT_GREATE_USER}", data=payload)

        r = response.json()
        s = r['success']

        assert response.status_code == 403 and s is False

    @pytest.mark.parametrize('input',[
        '{"email":"Saya6@gmail.com", "password": "12345"}',
        '{"email": "Saya6@gmail.com", "name": "Saya"}',
        '{"password": "12345", "name": "Saya"}'
    ])
    @allure.step('Неуспешное создание  пользователя без одного поля')
    def test_create_user_missing_one_field(self, input):

        response = requests.post(f"{URL}{ENDPOINT_GREATE_USER}", data=input)

        r = response.json()
        s = r['success']

        assert response.status_code == 403 and s is False

