### RUTAS CON PARAMETROS

en "urls.py" para ponerle parametros a una ruta
(path) hay que hacerlo de la siguiente manera:

path('nombre/<dataType: parameter>/')

### USO DE PLANTILLAS

para usar plantillas html en Django, debemos ir a "settings.py" buscar el array "DIR" y añadir la carpeta en la que se almacenaran nuestros templates.

para que sea posible la vista del template, en "views.py" hay que importar el metodo render() de Django y retornarlo en una vista pasandole como parametros el request y el archivo html.

### USO DE CONTEXTOS

basicamente, lo que entendi, es que el contexto son las variables que le pasamos al template. Se la pasamos en forma de un diccionario.
Conforme vaya aprendiendo mas actualizare las notas.

### BUCLES Y CONDICIONALES EN LAS PLANTILLAS.

para añadir logica de python a documentos html debemos escribir:
{{% OPERACION_LOGICA %}}
    codigo
{{% END_OPERACION_LOGICA %}}

### COMENTARIOS Y FILTROS.

Si bien podemos añadir comentarios normales, en plan HTML (<-- -->),
este queda expuesto al usuario. Los comentarios de python, no.

tenemos dos formas de hacerlo: comentario simple y multilinea.

EL SIMPLE: {# COMENTARIO #}

MULTILINEA: {# comment #}
                el texto despues de esta etiqueta se interpreta como
                comentario de python, hasta que se lea la etiqueta de 
                end
            {# endcomment #}
    
En el tema de filtros hay muchisimo por anotar, en resumen:
    son "metodos" que se le pueden añadir a las variables
    en las templates escribiendo "|" luego de la variable.

    Se pueden anidar.
