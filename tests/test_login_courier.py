import allure
import pytest
from methods.base_api import BaseApi
from methods.login_courier_api import LoginCourierApi
from data.login_courier_data import LoginCourierData

class TestLoginCourier:
    @allure.title('курьер может авторизоваться')
    def test_login_courier(self, generate_random_string):
        login = generate_random_string
        password = generate_random_string
        first_name = generate_random_string
        response_create = BaseApi.post_create_courier(login, password, first_name)
        response_login = LoginCourierApi.post_login_courier(login,password)
        with allure.step('Проверяем код и текст ответа'):
            assert response_login.status_code == 200 and LoginCourierData.TEXT_LOGIN_COURIER_200 in response_login.text

    @allure.title('для авторизации нужно передать все обязательные поля, не передан логин')
    def test_login_courier_no_login_error(self, generate_random_string):
        login = generate_random_string
        password = generate_random_string
        first_name = generate_random_string
        response_create = BaseApi.post_create_courier(login, password, first_name)
        response_login = LoginCourierApi.post_login_courier('',password)
        with allure.step('Проверяем код и текст ответа'):
            assert response_login.status_code == 400 and  response_login.text == LoginCourierData.TEXT_LOGIN_COURIER_400

    @allure.title('для авторизации нужно передать все обязательные поля, не передан пароль')
    def test_login_courier_no_password_error(self, generate_random_string):
        login = generate_random_string
        password = generate_random_string
        first_name = generate_random_string
        response_create = BaseApi.post_create_courier(login, password, first_name)
        response_login = LoginCourierApi.post_login_courier(login,'')
        with allure.step('Проверяем код и текст ответа'):
            assert response_login.status_code == 400 and  response_login.text == LoginCourierData.TEXT_LOGIN_COURIER_400

    @allure.title('если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    def test_login_courier_no_exist_courier_error(self):
        response_login = LoginCourierApi.post_login_courier('Akimov_test','123')
        with allure.step('Проверяем код и текст ответа'):
            assert response_login.status_code == 404 and  response_login.text == LoginCourierData.TEXT_LOGIN_COURIER_404

    @allure.title('система вернёт ошибку, если неправильно указать пароль')
    def test_login_courier_wrong_password_error(self,generate_random_string):
        login = generate_random_string
        password = generate_random_string
        first_name = generate_random_string
        response_create = BaseApi.post_create_courier(login, password, first_name)
        response_login = LoginCourierApi.post_login_courier(login,'123')
        with allure.step('Проверяем код и текст ответа'):
            assert response_login.status_code == 404 and  response_login.text == LoginCourierData.TEXT_LOGIN_COURIER_404