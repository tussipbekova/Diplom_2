import allure
import requests

from conftest import register_new_user_and_return_email_password
from data import URL, ENDPOINT_CHANGE_USER_DATA, ENDPOINT_LOGIN_USER


@allure.title('Изменение данных пользователя')
class TestChangingUserData:
    @allure.step('Изменение данных пользователя с авторизацией')
    def test_changing_user_data_with_authorization(self, register_new_user_and_return_email_password):
        email, password, name = register_new_user_and_return_email_password

        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(f"{URL}{ENDPOINT_LOGIN_USER}", data=payload)

        assert response.status_code == 200

        r = response.json()
        at = r['accessToken']

        payload = {
            "email": email,
            "name": "Saya"
        }

        response = requests.patch(f"{URL}{ENDPOINT_CHANGE_USER_DATA}", headers={
    'Authorization': at}, data=payload)

        assert response.status_code == 200

        @allure.step('Изменение данных пользователя без авторизации')
        def test_changing_user_data_without_authorization(self):

            payload = {
                "email": "saya10.test@yandex.ru",
                "name": "Saya"
            }

            response = requests.patch(f"{URL}{ENDPOINT_CHANGE_USER_DATA}", data=payload)

            assert response.status_code == 401





