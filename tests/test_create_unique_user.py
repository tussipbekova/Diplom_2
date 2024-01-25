import allure
import requests

from data import URL, ENDPOINT_GREATE_USER


@allure.title('Создание пользователя')
class TestCreateUser:
    @allure.step('Cоздание уникального пользователя')
    def test_create_unique_user(self,generate_random_string):
        name = generate_random_string
        email = generate_random_string+'@yandex.ru'
        password = generate_random_string

        payload = {
            "email": email,
            "password": password,
            "name": name
        }

        response = requests.post(f"{URL}{ENDPOINT_GREATE_USER}", data=payload)

        assert response.status_code == 200

    @allure.step('Cоздание уже зарегистрированного пользователя')
    def test_create_registered_user(self,generate_random_string):

        payload = {
            "email": "Saya.test@yandex.ru",
            "password": 'Saya789',
            "name": 'Saya'
        }

        response = requests.post(f"{URL}{ENDPOINT_GREATE_USER}", data=payload)

        assert response.status_code == 403

    @allure.step('Cоздание  пользователя без одного поля(например логина)')
    def test_create_user_missing_login(self, generate_random_string):
        email = generate_random_string + '@yandex.ru'
        password = generate_random_string

        payload = {
            "email": email,
            "password": password,
        }

        response = requests.post(f"{URL}{ENDPOINT_GREATE_USER}", data=payload)

        assert response.status_code == 403

