import requests
import configuration


# запрос на создание нового заказа
def create_new_order(body):
    url = configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER
    response = requests.post(url, json=body)
    return response.json()["track"]

# запрос на получение заказа по треку
def get_order (track):
    url = configuration.URL_SERVICE + configuration.GET_ORDER
    response = requests.get(url, params={"t": track})
    return response
