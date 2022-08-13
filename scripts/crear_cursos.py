import click 
from app import app
from modelos import Usuario
from modelos import Curso
from passlib.hash import pbkdf2_sha256 as sha256

from .crear_usuarios import usuarios


@click.group
def cursos():
    '''Este grupo de scripts se encangar de crear usuarios de prueba para la aplicacion'''
    pass


@cursos.command("crear_cursos")
def crear_cursos():
    '''Crear cursos de prueba para los profesores de prueba. Para cada profesor se crean 5 cursos'''
    
    profes = Usuario.select().where(
        (Usuario.nickname.contains("profe-")) 
        &  # AND
        (Usuario.rol==Usuario.ROLES.PROFESOR.value)
    )

    print("......")
    for profe in profes:
        for i in range(5):
            try:
                Curso.create(
                    creador = profe,
                    nombre = f'curso-{i+1}-{profe.nickname}',
                    descripcion = 'Curso de prueba creado automaticamente para validad el funcionamientom correcto de la app',
                    url_foto = 'https://1.bp.blogspot.com/-sffTqPYtaHY/Xl5hm6h8CQI/AAAAAAAAcew/KPScjjXwwgkQT-5spxLURf01P7RPbke8ACLcBGAsYHQ/s1600/12.png',
                    # url_foto = "https://learnenglishteens.britishcouncil.org/sites/teens/files/rs163_91459369-low.jpg"
                )
                print("Curso creado con exito")
            except Exception as e:
                print(f"Erro: {e}")
