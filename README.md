# Proyecto: Urban-Grocers  
## *Automatización de las pruebas.*
	
![image](https://github.com/user-attachments/assets/43ce7d9a-083e-470a-ae8d-869b46fbe672)


### :page_facing_up: *Documentación utilizada:* 
- Requisitos para el back-end de Urban Grocers: [Link de Requisitos](https://practicum-content.s3.us-west-1.amazonaws.com/new-markets/qa-sprint-3/QA_3.1.1_Requisitos_para_el_back-end_de_Urban.grocers.pdf)
- Dirección del servidor: [Link de aplicacion](https://3cd0a718-aa1b-46c4-86bd-318797f0fda9.containerhub.tripleten-services.com)
- Apidocs, documentación de la API:  [Link de Apidocs](https://cnt-e32613b1-6474-4625-97fd-10811052e478.containerhub.tripleten-services.com/docs/)

### 🛠️ *Lenguajes y herramientas utilizadas:*
<div id="header" align="left">
    
- Jira: Registro y seguimiento de errores.
- Apidocs: Revisión de documentación de API's
- Postman: Pruebas manuales.
- HTTP: protocolo.
- REST: estructura.
- JSON: Formato para solicitudes REST.
- Diseño de pruebas para la API.
- Python: Codigo para las pruebas.
- Pycharm: Ejecución y automatización de las pruebas.
- GitBash: Clonación del repositorio.
- GitHub: Respaldo del codigo.
- Selenium, - Pytest, - Pip
- MS Office: Documentación de las pruebas.
  
</a>
<img decoding="async" src="https://img.shields.io/badge/Jira-0052CC?style=for-the-badge&logo=Jira&logoColor=white" alt="Jira"/>
<img decoding="async" src="https://img.shields.io/badge/Apidocs-darkblue?style=for-the-badge&logo=Apidocs&logoColor=white" alt="Apidocs"/>
<img decoding="async" src="https://img.shields.io/badge/Postman-D83B01?style=for-the-badge&logo=Postman&logoColor=white" alt="Postman"/>
<img decoding="async" src="https://img.shields.io/badge/HTTP-890000?style=for-the-badge&logo=HTTP&logoColor=white" alt="HTTP"/>
<img decoding="async" src="https://img.shields.io/badge/REST-black?style=for-the-badge&logo=REST&logoColor=white" alt="REST"/>
<img decoding="async" src="https://img.shields.io/badge/JSON-purple?style=for-the-badge&logo=JSON&logoColor=white" alt="JSON"/>
<img decoding="async" src="https://img.shields.io/badge/Python-0052CC?style=for-the-badge&logo=python&logoColor=white" alt="python"/>
<img decoding="async" src="https://img.shields.io/badge/PyCharm-darkgreen.svg?&style=for-the-badge&logo=PyCharm&logoColor=white" alt="PyCharm"/>
<img decoding="async" src="https://img.shields.io/badge/Git_Bash-D89B01?&style=for-the-badge&logo=GitBash&logoColor=white" alt="GitBash"/>
<img decoding="async" src="https://img.shields.io/badge/GitHub-000000.svg?&style=for-the-badge&logo=GitHub&logoColor=white" alt="GitHub"/>
<img decoding="async" src="https://img.shields.io/badge/Selenium-008000?style=for-the-badge&logo=Selenium&logoColor=white" alt="Selenium"/>
<img decoding="async" src="https://img.shields.io/badge/Pytest-darkblue?style=for-the-badge&logo=pytest&logoColor=white" alt="pytest"/>
<img decoding="async" src="https://img.shields.io/badge/Pip-darkgreen?style=for-the-badge&logo=Pip&logoColor=white" alt="Pip"/>
<img decoding="async" src="https://img.shields.io/badge/Microsoft_Office-D86B01?style=for-the-badge&logo=microsoft-office&logoColor=white" alt="microsoft-office"/>
</a>

### :fireworks: *Descripción del Backend (API) Urban Grocers*
- El área de desarrollo ha agregado una nueva función en la API de Urban.Grocers, así que pasaron una nueva versión de la API para que la pruebes. La aplicación permite realizar pedidos y entrega de productos por catalogo. Para la automatización y revisión del Banckend, se realizó una lista de comprobación de elementos con un total de 9 items. Se ejecutaron las pruebas automatizadas del aplicativo, utilizando solicitudes HTTP y en formato JSON para gestionar la creación de kit, comprobando la funcionalidad del campo *"name"*. A continuación, se enlistan cada una de las pruebas con sus especificaciones.

### :paw_prints: *Pasos a seguir para la ejecución de las pruebas:* 

- Conexión al servidor medienta la URL.
- Analisis de requisitos.
- Elaboración de lista de comprobación.
- Protocolo HTTP
- Solicitudes en formato JSON.
- Estructura REST
- Ejecución de las pruebas.
  
### :page_facing_up: *Lista de Comprobación de Pruebas:*  
- Endpoints probados
  - [POST] /api/v1/kits (Crear kit vacio) Campo **Name**
	
1.- El número permitido de caracteres (1): kit_body = { "name": "a"}	
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud.

2.- El número permitido de caracteres (511): kit_body = { "name":"El valor de prueba para esta comprobación será     inferior a"}	
    Código de respuesta: 201 El campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud

3.- El número de caracteres es menor que la cantidad permitida (0): kit_body = { "name": "" }	
    Código de respuesta: 400

4.- El número de caracteres es mayor que la cantidad permitida (512): kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }	
    Código de respuesta: 400

5.- Se permiten caracteres especiales: kit_body = { "name": ""№%@"," }	
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

6.- Se permiten espacios: kit_body = { "name": " A Aaa " }	
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

7.- Se permiten números: kit_body = { "name": "123" }	
    Código de respuesta: 201 El campo "name" del cuerpo de la respuesta coincide con el campo "name" del cuerpo de la solicitud

8.- El parámetro no se pasa en la solicitud: kit_body = { } Código de respuesta: 400

9.- Se ha pasado un tipo de parámetro diferente (número): kit_body = { "name": 123 } Código de respuesta: 400

### :file_folder: *Archivos:* 
1. README (Descripcion del contenido)
2. configuration.py (url y endpoints)
3. Data.py (Datos de las pruebas)
4. sender_stand_request.py (métodos para las pruebas)
5. create_kit_name_kit_test.py (funciones de las prueba)

### :paw_prints: *Pasos a seguir:* 

- Se guardan las rutas en el archivo configuration.py
- Se guardan los datos de los cuerpos de la solicitud POST en el archivo data.py
- Se crean las funciones en el archivo sender_stand_request.py
- Se crea la función para crear un nuevo usuario y nos devuelve el token de autorización, enviando una solicitud post, utilizando el body con los datos del usuario que se encuentra en data.
- Se crea la función get_new_user_token para recibir el authToken y tomar la clave de autenticación, llamando la variable con el post de la creación del usurio.
- Se crea l afunción post_new_client_kit para crear un kit, enviando una solicitud post, que requiere el token de autenticación y el nombre del kit(name) junto con el encabezado en return.
- Se crea la función para las pruebas positivas de nuestra lista de comprobación positive_assert del kit, usando los parametros del nombre (name) y el token para las pruebas del campo (name). Esperando un codigo de respuesta 201.
- Se crea la función para las pruebas negativas de nuestra lista de comprobación negative_assert_code_400 del kit, sando los parametros del nombre (name) y el token para las pruebas del campo (name). Esperando un codigo de respuesta 400.
- Se guardan las funciones para pruebas en el archivo create_kit_name_kit_test.py
- Se crean las 10 funciones de prueba con la palabra "test" cambiando las clases de equivalencias para el campo "name" de acuerdo a los requisitos y la lista de comprobación; tanto para pruebas negativas como positivas.
       
<div id="header" align="center"> 
  
![image](https://github.com/user-attachments/assets/53cbe0da-08d5-4a40-af07-c484873119d1)
