import requests
import configuration
import data


# solicitud para crear un usuario y nos devuelve el token de autorización
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


# recibimos el authToken y solo tomamos la clave
def get_new_user_token():
    response = post_new_user(data.user_body.copy())
    response_json = response.json()
    return response_json["authToken"]


# esta solicitud crea un kit, para lo cual nos pide los parametros de kit_body, auth_token y headers
def post_new_client_kit(kit_body, auth_token):
    headers = data.headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KITS_PATH,
                         json=kit_body,
                         headers=headers
                         )


# esta es la función para las pruebas positivas
def positive_assert(kit_body):
    kit_response = post_new_client_kit(kit_body, get_new_user_token())  # esta variable almacena lo que responde post
    assert kit_response.status_code == 201  # compara que el codigo del kit sea igual a 201
    assert kit_response.json()["name"] == kit_body["name"]  # compara el nombre del kit con el nombre del kit enviado


# esta es la función para las pruebas negativas
def negative_assert_code_400(kit_body):
    response = post_new_client_kit(kit_body, get_new_user_token()) # esta variable almacena lo que responde post
    assert response.status_code == 400  # compara que el codigo del kit sea igual a 400
