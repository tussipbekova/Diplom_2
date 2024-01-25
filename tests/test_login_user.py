import allure
import requests

from data import URL, ENDPOINT_LOGIN_USER


@allure.title('Авторизация пользователя')
class TestLoginUser:
    @allure.step('Авторизация под существующим пользователем')
    def test_login_user(self, register_new_user_and_return_email_password):
        email, password, name = register_new_user_and_return_email_password

        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(f"{URL}{ENDPOINT_LOGIN_USER}", data=payload)

        assert response.status_code == 200