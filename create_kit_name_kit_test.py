import sender_stand_request
import data


# Prueba positiva 1
# El número permitido de caracteres (1): kit1 = { "name": "a"}
def test_create_new_kit_one_character_get_success_response():
    sender_stand_request.positive_assert(data.kit1)


# Prueba positiva 2
# El número permitido de caracteres (511): kit2 = { "name":"inferior a"}
def test_create_new_kit_511_character_get_success_response():
    sender_stand_request.positive_assert(data.kit2)


# Prueba negativa 3
# El número de caracteres es menor que la cantidad permitida (0): kit3 = { "name": "" }
def test_create_new_kit_null_character_get_error_response():
    sender_stand_request.negative_assert_code_400(data.kit3)


# Prueba negativa 4
# El número de caracteres es mayor que la cantidad permitida (512): kit4 = { "name":"inferior a” }
def test_create_new_kit_512_more_character_get_error_response():
    sender_stand_request.negative_assert_code_400(data.kit4)


# Prueba positiva 5
# Se permiten caracteres especiales: kit5 = { "name": ""№%@"," }
def test_create_new_kit_special_symbol_character_get_error_response():
    sender_stand_request.positive_assert(data.kit5)


# Prueba positiva 6
# Se permiten espacios: kit6 = { "name": " A Aaa " }
def test_create_new_kit_has_space_character_get_error_response():
    sender_stand_request.positive_assert(data.kit6)


# Prueba positiva 7
# 	Se permiten números: kit7 = { "name": "123" }
def test_create_new_kit_has_number_name_get_error_response():
    sender_stand_request.positive_assert(data.kit7)


# Prueba negativa 8
# El parámetro no se pasa en la solicitud: kit8 = { }
def test_create_new_kit_empty_name_get_error_response():
    sender_stand_request.negative_assert_code_400(data.kit8)


# Prueba negativa 9
# Se ha pasado un tipo de parámetro diferente (número): kit9 = { "name": 123 }
def test_create_user_number_type_first_name_get_error_response():
    sender_stand_request.negative_assert_code_400(data.kit9)

