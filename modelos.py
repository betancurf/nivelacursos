import email
from email.policy import default
from random import choices
from peewee import *
from playhouse.flask_utils import FlaskDB
from uuid  import uuid4
from strenum import StrEnum
from enum import auto
from flask_login import UserMixin

db = FlaskDB()


class Usuario(db.Model, UserMixin):
    class ROLES(StrEnum):
        ADMIN = auto()
        PROFESOR = auto()
        ESTUDIANTE = auto()
    
    '''
    Usar ENUMS nos permite asociar una valor o codigo con un nombre, de
    tal forma que siempre que requiera asignar un codigo que es dificil 
    de recordad puedo usar su nombre y el objeto enum me da su codigo o valor
    asigando.

    Es el equivalente a tener algo como esto:
    class ROLES():
        ADMIN=1
        PROFESOR=2
        ESTUDIANTE=3
    
    o como esto:
    ROLES=[
        ["ADMIN", 1]
        ["PROFESOR", 2]
        ["ESTUDIANTE", 3]
    ]

    Adicionalemente, la clase StrEnum me permite asociar valores o codigo
    en formato de string. Empleando "auto()" este valor se asigna automaticamente
    igual al nombre. Esto nos ahorra el problema de no tener valores estandarizados.
    Ejemplo: 
    
    Fabian.rol  = "Profesor"
    Laura.rol   = "Profesora"
    Maira.rol   = "Docente"
    Mauricio.rol  = "Profe"
    Juan.rol    = "ProFeSor"
    '''

    id = UUIDField(primary_key=True, default=uuid4)
    nickname = CharField(unique=True, default="N/A")
    correo = CharField(unique=True)
    password = CharField(default="1234")
    nombre = CharField(null=True)
    apellidos = CharField(null=True)
    telefono = CharField(null=True)
    rol = CharField(
        default=ROLES.ESTUDIANTE.value,
        choices=[(r.name, r.value) for r in ROLES]
    )


class Curso(db.Model):
    id = UUIDField(primary_key=True, default=uuid4)
    creador = ForeignKeyField(Usuario, backref="cursos_creados")
    nombre = CharField()
    descripcion = CharField(null=True)
    url_foto = CharField()


class UsuarioCurso(db.Model):
    usuario = ForeignKeyField(Usuario)
    curso = ForeignKeyField(Curso)
    nota = FloatField(default=0)


class PQR(db.Model):
    id = UUIDField(primary_key=True, default=uuid4)
    nombre = CharField()
    email = CharField()
    asunto = CharField()
    mensaje = CharField(max_length=1000)
