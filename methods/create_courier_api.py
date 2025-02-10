import requests
from urls.urls import Urls

class CreateCourierApi:
    @staticmethod
    def post_create_courier(login,password,first_name):
        response = requests.post(Urls.URL_CREATE_COURIER,data={"login":login,"password":password,"firstName":first_name})
        return response