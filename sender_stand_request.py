import json
import requests
import configuration
import data


"""este metodo me devuelve el token del usuario"""
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


#response = post_new_user(data.user_body)
#print(response.json())


"""recibimos el authToken y solo sacamos el valor del mismo"""


def get_new_user_token():
    response = post_new_user(data.user_body.copy())
    response_json = response.json()
    return response_json["authToken"]


#print("esto es del get new user")
#respuesta1 = get_new_user_token()
#print(respuesta1)


"""me crea un nuevo kit"""


def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=headers
                         )


resp2 = post_new_client_kit(data.kit_body, get_new_user_token())
#resp = resp2.json()
print("esto es para la creacion de un nuevo kit")
print(resp2.json())
print(resp2.url)
#print(resp.json['name'])


def positive_assert(name): # "kit1": {"name": "a"}
    kit_response = post_new_client_kit(name, get_new_user_token()) # almacena lo que responde post
    assert kit_response.status_code == 201 # compara que el codigo del kit sea igual a 201
    assert kit_response.json()["name"] == name["name"] # compara el nombre del kit con el nombre del kit enviado



"""def get_kit_body(name):
    current_body = data.kit_body.copy()
    #current_body.json["name"] = name
    return current_body.json["name"]"""