### ARCHIVOS ESTATICOS.

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

link rel="stylesheet" href="{% static 'style.css' %}"


### HERENCIA DE PLANTILLAS.

En todos los apuntes digo lo mismo, pero esto es importantisimo.

Es la solucion para la re-escritura de codigo.

En el directorio "templates", crear una nueva carpeta, para el ejemplo: 
"layouts", ahi crear la plantilla base.

En esta plantilla base escribiríamos el código que vamos a utilizar en todos
nuestros demás archivos.

Ahora, para introducir nuestras "variables" por asi llamar al codigo que irá
mutando de archivo en archivo, escribimos:

                        {% block VARIABLE %}

Luego, creamos el archivo nuevo (HTML) y para pasarle la plantilla introducimos al comienzo del código:

                        {% extends './layouts/base.html' %}

Por último para rellenar el contenido de estas variables, en el archivo nuevo podriamos por ejemplo hacer:

                            {% block content %}
                                <h1>Herencias</h1>
                            {% endblock %}