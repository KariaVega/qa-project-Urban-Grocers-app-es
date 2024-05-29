import sender_stand_request
import data


# Prueba 1 El número permitido de caracteres (1): kit_body_class = { "name": "a"}
def test_create_new_kit_one_character_get_success_response():
    sender_stand_request.positive_assert(data.kit_body_class['kit1'])


# Prueba positive 2
def test_create_new_kit_511_character_get_success_response():
    sender_stand_request.positive_assert(data.kit_body_class['kit2'])


# Prueba negative 3
def test_create_new_kit_null_character_get_error_response():
    sender_stand_request.negative_assert_code_400(data.kit_body_class['kit3'])


# Prueba negative 4
def test_create_new_kit_512_more_character_get_error_response():
    sender_stand_request.negative_assert_code_400(data.kit_body_class['kit4'])


# Prueba negative 5
def test_create_new_kit_special_symbol_character_get_error_response():
    sender_stand_request.positive_assert(data.kit_body_class['kit5'])


# Prueba negative 6
def test_create_new_kit_has_space_character_get_error_response():
    sender_stand_request.positive_assert(data.kit_body_class['kit6'])


# Prueba negative 7
def test_create_new_kit_has_number_name_get_error_response():
    sender_stand_request.positive_assert(data.kit_body_class['kit7'])


# Prueba negative 8
def test_create_new_kit_empty_name_get_error_response():
    sender_stand_request.negative_assert_code_400(data.kit_body_class['kit8'])


# Prueba negative 9
def test_create_user_number_type_first_name_get_error_response():
    sender_stand_request.negative_assert_code_400(data.kit_body_class['kit9'])

