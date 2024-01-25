import random
import string


import pytest
import requests


@pytest.fixture(scope="function")
def generate_random_string():
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(10))
    return random_string

@pytest.fixture(scope="function")
def register_new_user_and_return_email_password(generate_random_string):

    # создаём список, чтобы метод мог его вернуть
    email_pass = []

    # генерируем логин, пароль и имя курьера
    email = generate_random_string+'@yandex.ru'
    password = generate_random_string
    name = generate_random_string

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)

    email_pass.append(email)
    email_pass.append(password)
    email_pass.append(name)

    return email_pass