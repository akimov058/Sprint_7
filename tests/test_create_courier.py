import allure
import requests
import pytest
from methods.base_api import BaseApi
from data.base_page_data import BasePageData

class TestCreateCourier:

    @allure.title('курьера можно создать')
    def test_create_courier(self,generate_random_string):
        login = generate_random_string
        password = generate_random_string
        first_name = generate_random_string
        response = BaseApi.post_create_courier(login,password,first_name)
        assert response.status_code==201 and response.text == BasePageData.TEXT_CREATE_COURIER_201

    @allure.title('нельзя создать двух одинаковых курьеров')
    def test_create_courier_create_two_courier_error(self,generate_random_string):
        login = generate_random_string
        password = generate_random_string
        first_name = generate_random_string
        response = BaseApi.post_create_courier(login,password,first_name)
        response_error = BaseApi.post_create_courier(login, password, first_name)
        assert response_error.status_code==409 and response_error.text == BasePageData.TEXT_CREATE_COURIER_409

    @allure.title('чтобы создать курьера, нужно передать в ручку все обязательные поля, не заполнен логин')
    def test_create_courier_no_login_error(self, generate_random_string):
        login = ''
        password = generate_random_string
        first_name = generate_random_string
        response = BaseApi.post_create_courier(login, password, first_name)
        assert response.status_code == 400 and response.text == BasePageData.TEXT_CREATE_COURIER_400

    @allure.title('чтобы создать курьера, нужно передать в ручку все обязательные поля, не заполнен пароль')
    def test_create_courier_no_password_error(self, generate_random_string):
        login = generate_random_string
        password = ''
        first_name = generate_random_string
        response = BaseApi.post_create_courier(login, password, first_name)
        assert response.status_code == 400 and response.text == BasePageData.TEXT_CREATE_COURIER_400
