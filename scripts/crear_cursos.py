import click 
from app import app
from modelos import Usuario
from passlib.hash import pbkdf2_sha256 as sha256


@click.group
def cursos():
    '''Este grupo de scripts se encangar de crear usuarios de prueba para la aplicacion'''
    pass


@cursos.command("crear_cursos")
def crear_cursos():
    '''En construccion ....'''
    pass

# '''
# Este script permite crear cursos fake para hacer pruebas
# Requiere:
# - id de un usuario de la base de datos
# - ulr de una foto 
# '''

# from uuid import uuid4

# id_usuario = '166ef762d27d480880ecc4168f0ba20c'
# url_foto = 'https://learnenglishteens.britishcouncil.org/sites/teens/files/rs163_91459369-low.jpg'
# cantidad = 10


# for i in range(cantidad):
#     query = f"""
#     INSERT INTO "main"."curso"
#     ("id", "creador_id", "nombre", "descripcion", "url_foto")
#     VALUES ('{uuid4()}', '{id_usuario}', 'Curso {i}', 'Curso test', '{url_foto}');
#     """

#     print(query)
#     print()






