import requests
from urls.urls import Urls

class LoginCourierApi:
    @staticmethod
    def post_login_courier(login,password):
        payload = {"login":login,"password":password}
        response = requests.post(Urls.URL_LOGIN_COURIER,data=payload)
        return response