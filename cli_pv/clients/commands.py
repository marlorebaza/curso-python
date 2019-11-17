import click

from clients.services import ClientService
from clients.models import Client

@click.group()
def clients():
    """ Manages the clients lifecycle """
    pass

@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help='The client name')
@click.option('-c', '--company', type=str, prompt=True, help='The client company')
@click.option('-e', '--email', type=str, prompt=True, help='The client email')
@click.option('-p', '--position', type=str, prompt=True, help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
    """ Creates new client """
    client = Client(name, company, email, position)
    client_service = ClientService(ctx.obj['client_table'])
    client_service.create_client(client)
    click.echo('Client created.')


@clients.command()
@click.pass_context
def list(ctx):
    """ List all clients """
    client_service = ClientService(ctx.obj['client_table'])
    click.echo('UID    |    NAME    |    COMPANY    |    EMAIL    |    POSITION')
    clients = client_service.list_clients()
    for client in clients:
        click.echo('{uid}    |    {name}    |    {company}    |    {email}    |    {position}'
                   .format(
                       uid=client['uid'], 
                       name=client['name'], 
                       company=client['company'], 
                       email=client['email'], 
                       position=client['position']))


@clients.command()
# el primer parámetro enviado a @argument debe ser igual al nombre del parámetro con el que hará match en la función
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx, client_uid):
    """ Updates a client """
    client_service = ClientService(ctx.obj['client_table'])
    
    client = _get_client(client_service.list_clients(), client_uid)
    
    if client:
        # desempaquetamos ciente encontrado (key: value) para enviarlo al constructor de Client
        client = _update_client_flow(Client(**client))
        client_service.update_client(client)
        click.echo('Client updated.')
    else:
        click.echo('Client not found.')


def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value')
    
    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position= click.prompt('New position', type=str, default=client.position)
    
    return client


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def delete(ctx, client_uid):
    """ Deletes a client """
    client_service = ClientService(ctx.obj['client_table'])
    
    client = _get_client(client_service.list_clients(), client_uid)
    
    if client:
        client_service.delete_client(client)
        click.echo('Client deleted.')
    else:
        click.echo('Client not found.')
        
        
def _get_client(clients, client_uid):
    return next(filter(lambda c: c['uid'] == client_uid, clients), None)
    

all = clients
