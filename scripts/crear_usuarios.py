import click 
from app import app
from modelos import Usuario
from passlib.hash import pbkdf2_sha256 as sha256


@click.group
def usuarios():
    '''Este grupo de scripts se encangar de crear usuarios de prueba para la aplicacion'''
    pass

@usuarios.command("crear_admin")
def crear_admin():
    '''Este comando crear el usuario administrador con nickname=admin y contraseña=admin. Si ya existe lo sobre escribe con los valores por defecto'''
    
    try:
        admin = Usuario.get(nickname="admin")
        print("El usuario Admin ya existe... se actualizan sus datos")
        admin.correo = "admin@admin.com"
        admin.password = sha256.hash("admin")
        admin.rol = Usuario.ROLES.ADMIN.value
        admin.save()
    except Exception as e:
        Usuario.create(
            nickname="admin",
            correo="admin@admin.com",
            password=sha256.hash("admin"),
            rol=Usuario.ROLES.ADMIN.value
        )
        print("Usuario creado con exito")


@usuarios.command("crear_profesores")
def crear_profesores():
    '''Este comando crear 10 profesores con nickname="profe-<numero>" y pass="profe-<numero>". Si el profesor con ese Nick ya existe, lo sobre escribe con los valores por defecto'''
    for i in range(10):
        nombre = f"profe-{i+1}"
        try:
            profe = Usuario.get(nickname=nombre)
            print(f"El usuario {nombre} ya existe... se sobre escribirá con los valores por defecto")
            profe.correo = f"{nombre}@{nombre}.com"
            profe.password = sha256.hash(nombre)
            profe.rol = Usuario.ROLES.PROFESOR.value
            profe.save()
        except Exception as e:
            Usuario.create(
                nickname=nombre,
                correo=f"{nombre}@{nombre}.com",
                password=sha256.hash(nombre),
                rol=Usuario.ROLES.PROFESOR.value
            )
            print(f"{nombre} creado con exito")

@usuarios.command("crear_estudiantes")
def crear_estudiantes():
    '''Este comando crear 10 profesores con nickname="est-<numero>" y pass="est-<numero>". Si el estudiante con ese Nick ya existe, lo sobre escribe con los valores por defecto'''
    for i in range(10):
        nombre = f"est-{i+1}"
        try:
            profe = Usuario.get(nickname=nombre)
            print(f"El usuario {nombre} ya existe... se sobre escribirá con los valores por defecto")
            profe.correo = f"{nombre}@{nombre}.com"
            profe.password = sha256.hash(nombre)
            profe.rol = Usuario.ROLES.PROFESOR.value
            profe.save()
        except Exception as e:
            Usuario.create(
                nickname=nombre,
                correo=f"{nombre}@{nombre}.com",
                password=sha256.hash(nombre),
                rol=Usuario.ROLES.PROFESOR.value
            )
            print(f"{nombre} creado con exito")
