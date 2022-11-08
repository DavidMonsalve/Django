### ARCHIVOS ESTATICOS

Esta es una parte MUY IMPORTANTE.
Esta relacionada con como conectamos nuestro template
a archivos CSS, de video, fotos, etc.

Debemos crear una carpeta llamada "static" en el
mismo directorio donde se encuentra la carpeta de 
templates.

dentro de esa carpeta introduciremos nuestro archivo que queremos
incluir en nuestro template.

Luego, en settings, abajo de "STATIC_URL", agregar:

 STATICFILES_DIRS = [
    BASE_DIR / "static",
]

Para vincular definitivamente el template del archivo, hay que ir al head del
template y escribir una "funcion en python" para que permita la carga de archivos estaticos:

{% load static %}

por ultimo, en head, escribir una etiqueta link y en el href introducir el directorio de nuestro archivo usando sintax de python:

<link rel="stylesheet" href="{% static 'style.css' %}">