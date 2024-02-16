import allure
import requests

from data import URL, ENDPOINT_LOGIN_USER, ENDPOINT_CREATING_AN_ORDER


@allure.title('Создание заказа')
class TestCreatingAnOrder:

    @allure.step('Создание заказа с авторизацией и с ингредиентами')
    def test_creating_an_order_with_authorization(self, register_new_user_and_return_email_password):
        email, password, name = register_new_user_and_return_email_password

        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(f"{URL}{ENDPOINT_LOGIN_USER}", data=payload)

        r = response.json()
        at = r['accessToken']

        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa70"]
        }

        response = requests.post(f"{URL}{ENDPOINT_CREATING_AN_ORDER}",headers={
            'Authorization': at}, data=payload)

        assert response.status_code == 200 and 'order' in response.json()

    @allure.step('Создание заказа без авторизации')
    def test_creating_an_order_without_authorization(self):

        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa70"]
        }

        response = requests.post(f"{URL}{ENDPOINT_CREATING_AN_ORDER}", data=payload)

        assert response.status_code == 200 and 'order' in response.json()

    @allure.step('Создание заказа без ингредиентов')
    def test_creating_an_order_with_ingredients(self,register_new_user_and_return_email_password):
        email, password, name = register_new_user_and_return_email_password

        payload = {
            "email": email,
            "password": password
        }
        response = requests.post(f"{URL}{ENDPOINT_LOGIN_USER}", data=payload)

        r = response.json()
        at = r['accessToken']

        payload = {
        }

        response = requests.post(f"{URL}{ENDPOINT_CREATING_AN_ORDER}", headers={
            'Authorization': at}, data=payload)

        r = response.json()
        s = r['success']

        assert response.status_code == 400 and s is False

    @allure.step('Создание заказа с неверным хэшем ингредиентов')
    def test_creating_an_order_with_false_ingredients(self):

        payload = {
            "ingredients": ["61c0c5a71d1f82001bdaaa6y"]
        }

        response = requests.post(f"{URL}{ENDPOINT_CREATING_AN_ORDER}", data=payload)

        assert response.status_code == 500





