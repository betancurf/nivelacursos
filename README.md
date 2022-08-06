# Nivelacursos

Proyecto falso para las clases de programación de ciclo 3, Uninorte.

## Instrucciones
- Si es la primera vez usando este proyecto:
    - Clonar el repo
    - Ejecutar
    ´´´bash
    pw_migrate migrate --database "sqlite:///db.sqlite3"
    ´´´

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
