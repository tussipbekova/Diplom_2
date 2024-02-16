import allure
import requests

from conftest import register_new_user_and_return_email_password
from data import URL, ENDPOINT_LOGIN_USER, ENDPOINT_CHANGE_AND_DELETE_USER_DATA


@allure.title('Изменение данных пользователя')
class TestChangingUserData:
    @allure.title('Изменение данных пользователя с авторизацией')
    def test_changing_user_data_with_authorization(self, register_new_user_and_return_email_password):
        email, password, name = register_new_user_and_return_email_password

        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(f"{URL}{ENDPOINT_LOGIN_USER}", data=payload)

        r = response.json()
        at = r['accessToken']

        payload = {
            "email": email,
            "name": "Saya"
        }

        response = requests.patch(f"{URL}{ENDPOINT_CHANGE_AND_DELETE_USER_DATA}", headers={
    'Authorization': at}, data=payload)

        r = response.json()
        s = r['success']

        assert response.status_code == 200 and s is True

    @allure.title('Изменение данных пользователя без авторизации')
    def test_changing_user_data_without_authorization(self):

        payload = {
                "email": "saya10.test@yandex.ru",
                "name": "Saya"
            }

        response = requests.patch(f"{URL}{ENDPOINT_CHANGE_AND_DELETE_USER_DATA}", data=payload)

        r = response.json()
        s = r['success']

        assert response.status_code == 401 and s is False





