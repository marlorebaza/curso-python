import click
from clients import commands as clients_commands 

CLIENTS_TABLE = '.clients.csv'

@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = {'client_table': CLIENTS_TABLE}
    # es lo mismo que:
    # ctx.obj = {}
    # ctx.obj['client_table'] = CLIENTS_TABLE

cli.add_command(clients_commands.all)


'''
Instalar:
- Hacerlo de preferencia en un ambiente virtual:
pip install --editable .
Le indicamos que instale lo que está dentro del directorio en modo editable, es decir los cambios
que vayamos haciendo al proyecto se verán reflejados a pesar de ya estar instalado.
"pip install ." hará uso de lo indicado en el archivo setup.py para la instalación del paquete 
'''