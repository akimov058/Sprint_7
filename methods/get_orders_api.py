import requests
from urls.urls import Urls

class GetOrdersApi:
    @staticmethod
    def get_orders():
        response = requests.get(Urls.URL_GET_ORDERS)
        return response