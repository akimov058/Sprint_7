import allure
import requests
from urls.urls import Urls
import pytest
from methods.create_courier_api import CreateCourierApi

class TestCreateCourier:

    @allure.title('курьера можно создать')
    def test_create_courier(self,generate_random_string):
        login = generate_random_string
        password = generate_random_string
        first_name = generate_random_string
        response = CreateCourierApi.post_create_courier(login,password,first_name)
        text = '{"ok":true}'
        assert response.status_code==201 and response.text == text