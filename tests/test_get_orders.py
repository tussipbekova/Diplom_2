import allure
import requests

from data import ENDPOINT_LOGIN_USER, URL, ENDPOINT_GET_ORDERS_AUTHORIZED_USER


@allure.title('Получение заказов конкретного пользователя')
class TestGetOrdersFromASpecificUser:

    @allure.step('Получение заказов авторизованного пользователя')
    def test_get_orders_authorized_user(self,register_new_user_and_return_email_password):
        email, password, name = register_new_user_and_return_email_password

        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(f"{URL}{ENDPOINT_LOGIN_USER}", data=payload)

        assert response.status_code == 200

        r = response.json()
        at = r['accessToken']

        response = requests.get(f"{URL}{ENDPOINT_GET_ORDERS_AUTHORIZED_USER}", headers={
            'Authorization': at})

        assert response.status_code == 200 and 'orders' in response.json()

    @allure.step('Получение заказов неавторизованного пользователя')
    def test_get_orders_an_unauthorized_user(self):

        response = requests.get(f"{URL}{ENDPOINT_GET_ORDERS_AUTHORIZED_USER}")

        r = response.json()
        s = r['success']

        assert response.status_code == 401 and s is False





