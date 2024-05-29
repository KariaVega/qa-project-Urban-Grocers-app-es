# Proyecto Urban Grocers 
Requerimientos:
  https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-3/QA_3.1.1_Requisitos_para_el_back-end_de_Urban.grocers.pdf

Documentación API de la aplicación de Urban Grocers:   
  https://cnt-f89586d0-d9cc-4140-8ed1-3e9b2d70080a.containerhub.tripleten-services.com/docs/

Lista de Comprobación de Pruebas:
	
1	El número permitido de caracteres (1): kit_body = { "name": "a"}	
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud.

2	El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será     inferior a"}	
    Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud

3	El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }	
    Código de respuesta: 400

4	El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }	
    Código de respuesta: 400

5	Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }	
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

6	Se permiten espacios: kit_body = { "name": " A Aaa " }	
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

7	Se permiten números: kit_body = { "name": "123" }	
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

8	El parámetro no se pasa en la solicitud: kit_body = { }	Código de respuesta: 400

9	Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 }	
    Código de respuesta: 400

Pasos a seguir:

1.- Se guardan las rutas en el archivo configuration.py

2.- Se guardan los datos de los cuerpos de la solicitud POST en el archivo data.py 

3.- Se crean las funciones en el archivo sender_stand_request.py 
     
    _. Se crea la función para crear un nuevo usuario y nos devuelve el token de autorización, enviando una solicitud post, utilizando el body con los datos del usuario que se encuentra en data.
    _. Se crea la función get_new_user_token para recibir el authToken y tomar la clave de autenticación, llamando la variable con el post de la creación del usurio.
    _. Se crea l afunción post_new_client_kit para crear un kit, enviando una solicitud post, que requiere el token de autenticación y el nombre del kit(name) junto con el encabezado en return.
    _. Se crea la función para las pruebas positivas de nuestra lista de comprobación positive_assert del kit, usando los parametros del nombre (name) y el token para las pruebas del campo (name). Esperando un codigo de respuesta 201.
    _. Se crea la función para las pruebas negativas de nuestra lista de comprobación negative_assert_code_400 del kit, sando los parametros del nombre (name) y el token para las pruebas del campo (name). Esperando un codigo de respuesta 400.

4.- Se guardan las funciones para pruebas en el archivo create_kit_name_kit_test.py

    _. Se crean las 10 funciones de prueba con la palabra "test" cambiando las clases de equivalencias para el campo "name" de acuerdo a los requisitos y la lista de comprobación; tanto para pruebas negativas como positivas.