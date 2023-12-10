# Грунин Егор, 11-й поток - Финальный проект. Инженер по тестированию плюс
import configuration
import requests
import data

def post_new_order():
    return requests.post(url=configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body,
                         headers=data.headers)

def get_order(get_order_body):
    return requests.get(url=configuration.URL_SERVICE + configuration.GET_ORDER_PATH,
                         params=get_order_body,
                         headers=data.headers)