### DELEGACION DE RUTAS.

Hay que ser muy cuidadosos a la hora de definir las rutas
en las aplicaciones dentro de los proyectos.

La mejor manera de "modularizar" o estructurar
las rutas de las apps es creando un documento
"urls.py" dentro de cada app, y alli, que cada
aplicacion gestione por su cuenta sus rutas.

Para que estas rutas sean legibles por el programa principal
en el documento "/project/project/urls.py", debemos:

    1) importar el include de django.path.
 
    2) Por ultimo, en la lista de urls añadir un nuevo path que se conecte con la app, tal que:


            path('comentarios/', include('comentarios.urls'))


En donde "comentarios" vendria siendo nuestra app. 
Por ende, "comentarios.urls" son las rutas que
controla nuestra app.


### CREACION DE DATOS.

Por convenciones de python cuando creamos una clase
debemos escribir el nombre en singular y con la
primera letra mayuscula. No es obligatorio pero,
mejora la legibilidad.

(en la carpeta models de la app dentro del proyecto en este caso)
El objeto basicamente se crea de la siguiente manera:

            from django.db import models

            class Comment(models.Model):

                atributos del objeto a los cuales le podemos pasar parametros

                def __str__(self):
                    return self.name

Para hacer instancias de este objeto, creamos una nueva vista llamada create, por ejemplo.
Dentro de la funcion create, le diriamos a python algo como:

            comment = Comment(name = "David", score = 5, comment = "esto es un comment")
            comment.save()

"comment" vendria siendo una instancia del objeto Comment y le pasamos como parametros
los datos a guardar el la base de datos.

ahora bien, para finalmente guardar los datos utilizamos el metodo "save()".

Tambien podemos utilizar la siguiente instruccion dentro del def en la view:
    
            comment = Comment.object.create(name = "alex")

De esta manera se guarda automaticamente en la base de datos. Sin necesidad del metodo "save()".


### BORRADO DE DATOS.

Para este caso, de la forma en que borraremos el dato sera la siguiente:

Creamos una vista nueva llamada delete, en las urls. En las views creamos tambien
su respectiva funcion.

dentro de la funcion delete, creamos una variable que contenga el comentario que queremos borrar.
estos lo logramos usando el metodo get, de nuestra clase objecto. Le pasamos por parametro un valor
que identifique a la instacia que queremos borrar, en este caso iremos con el "ID".

tal que nos quedaria algo asi:

            comment = Comment.objects.get(id = 1)

ahora, para borrarlo, nos bastaria con indicar:

            comment.delete()

De la misma forma que hicimos con el create, aca tambien podemos hacer un borrado directo, para ello,
usaremos la funcion filter, para limpiar del objeto Comment aquel dato que le pasemos por parametro:

            Comment.objects.filter(id=2).delete()


### ESCTRUCTURAS Y CLAVES FORANEAS.