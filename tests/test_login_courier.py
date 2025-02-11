import allure
import requests
import pytest
from methods.base_api import BaseApi
from data.base_page_data import BasePageData

class TestLoginCourier:
    @allure.title('курьер может авторизоваться')
    def test_login_courier(self, generate_random_string):
        login = generate_random_string
        password = generate_random_string
        first_name = generate_random_string
        response = BaseApi.post_create_courier(login, password, first_name)