# Nivelacursos

Proyecto falso para las clases de programación de ciclo 3, Uninorte.

## Instrucciones
- Si es la primera vez usando este proyecto:
    - Clonar el repo
    - Ejecutar
    ```bash
    pw_migrate migrate --database "sqlite:///db.sqlite3"
    ```

- Si vas a actualizar el proyecto:
    - Solicitar ser colaborador
    - ....
    - Para actulizar la base de datos:
        1. Modificar el archivo de modelos.py
        2. Crear la migración:
        ```bash
        $ pw_migrate create --auto --database "sqlite:///db.sqlite3"  --auto-source modelos <nombre_de_la_migracion>
        ``` 
        3. Aplicar la migracion
        ```bash
        $ pw_migrate migrate --database "sqlite:///db.sqlite3"
        ```

## Instrucciones para la entrega:
Enfocarse en creare un PMV (P=producto M=minimo V=viable)

Considero que pueden tomar esta ruta:
- PMV
    - regsitro
    - login
    - paginas estaticas
    - perfil de usuario
    - crear producto
    - crear producto en carrito (En la sesion)
    - roles de usuarios dados manualmente por base de datos
- Version alpha:
    - Simular la compra
        - Darle comprar al carrito
        - Los productos del carrito pasan al historial de compras del usuario
        - Eliminar el carrito
- Version beta (Hasta aquí es que lo que se pide que entreguen):
    - Admin admite y/o bannea vendores
    - Admin admite y/o bannea productos
    - Crear producto en carrito (En base de datos)
    - Subir al servidor
- Version final:
    ¡ Esto NO es necesario! solo es un preview de lo que pueden hacer en el futuro con esta app
    - Subida en servidor propio (alquilado) con dominio
    - Tener correo empresarial
    - Asociar correo empresarial a la app
    - Implementar sistema de chat
    - Implementar sistema de comentarios en los productos
    - Implementar sistema de calificación de los productos
    - etc
    - etc
    - etc

## Tareas
Tarea 0:
- Crear la cuenta de github 
- Aceptar ser colaborador del proyecto de Nivelacursos
- Clonar el repo 
- Solicitar ser colaborador en el repositorio enviándole un mensaje de Whatsapp al profesor con su usuario de github
- Crear llaves SSH o Token [aquí tienen un instructivo:](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)

Tarea 1:
- Hacer pull del repo remoto # git pull
- Crear una rama local # git checkout -b nombre_rama
- Añadir su nombre al README.md
- Hacer add # git add .
- Crear un commit # git commit -m "Agrega mi nombre"
- Crear una rama remota # git push -u origin nombre_rama_remota
- Enviar los cambios a la rama remota
- Avisarme que todo OK o si hay prob

Tarea 2:
- git checkout tu_rama
- git pull origin master  # Nos estamos trayendo la ultima versión de la master
- Solucionar los conflictos en la rama
- Crear un commit
- git push 
- Ir a github, y hacer un Pull Request

Tarea 3:
- Descargar el template: [Logis](https://bootstrapmade.com/logis-bootstrap-logistics-website-template/)
- Añadir los archivos estaticos al proyecto (carpeta assets dentro del  template pasa a llamarse static dentro del proyecto)
- Implementar las paginas asignadas por el profesor basado en el html del template
- Añadir la ruta de la pagina asignada a las rutas de la aplicación principal
- Direccionar adecuadamente los archivos estaticos empleando **{{url_for('static', filename='/ruta/del/archivo/dentro/de/la/carpeta/static')}}** 

Tarea 4:
- Implementar {% extends "base" %} en los archivos html indicados
- Hacer pull resquest

Tarea 5:
- Enviar información del frontend al backend
    - Usando formulario
    - Usando query string
- Implementar logica segun los datos enviados

Tarea 6:
- Implementar {% include "fragment" %} en los archivos html indicados
- Trabajar con Bases de datos usando Peewee
- Trabajar con Migraciones

Tarea 7:
- Creacion de usuario
- Login de usuario
- Paginas que requieren login

Tarea 8:
- Pagina para crear cursos
- Pagina para ver el detalle del curso
    - Inscribirse al curso
- En perfil deben salir:
    - los cursos creados
    - los cursos en los que estoy inscrito
    - Boton para solicitar ser profesor

Tarea 9:
- Bloquear rama master
- Crear admin:
    - Crear un usuario cualquiera
    - Ir a la base de datos y cambiar su ROL a "ADMIN"
    - Crear archivo templates/admin/administrar_profesores.html
        - Esta pagina debe tener una lista de las solicitudes de usuarios para ser profesores con dos botones/opciones:
            - Aceptar
            - Rechazar
        - Debe tener una lista de los profesores actuales con la opcion de "degradar"
    - Crear un modelo en modelos.py con el nombre "SolicitudSerProfesor" con estos campos:
        - id Solicitante
        - [fecha de solicitud](http://docs.peewee-orm.com/en/latest/peewee/models.html?highlight=table%20generation)
    - Crear archivo modulos/admin.py
        - crear una blueprint
        - registrarla en la app principal
        - crear un endpoint que rederice la pagina de administrar profesores
            - el endpoint debe enviar al template la lista de las solicitudes
            - el endpoint debe enviar al template la lista de los profesores actuales
        - Cuando se haga post a este endpoint:
            - Validar si el boton es para rechazar o para aceptar
            - Si se acepta se cambia el rol
            - independientemente si se acepta o no, se borra la solicitud

Tarea 10:
- Subir al servidor
- Mensajes flash
- Sesiones

## Creado por:

- Fabian Betancur, Profesor Universidad del Norte
- Juan David Caicedo Aponte Estudiante Administración de Sistemas Informáticos
- Laura Pinzon Moreno Ingeniera Ambiental 
- Natalia Morales, Estudiante Uninorte
- Diego Rodriguez, Uninorte
- Juan David Saa, Estudiante Mision Tic
- SGOLDYT
- [Mauricio Martinez](https://xhlar.com)
- santiago m, ingeniero mecatrónico

**Y todos los demás estudiantes de misión tic en Uninorte para ciclo3 en 2022.**
