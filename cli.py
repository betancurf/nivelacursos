from pydoc import cli
import click
from scripts.crear_usuarios import usuarios
from scripts.crear_cursos import cursos

@click.group()
def cli():
    '''Herramienta de linea de comando para el proyecto Nivela'''
    pass


if __name__=="__main__":
    cli.add_command(usuarios)
    cli.add_command(cursos)
    cli()
