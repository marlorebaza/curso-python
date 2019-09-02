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
@click.pass_context
def update(ctx, client_uid):
    """ Updates a client """
    pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
    """ Deletes a client """
    pass

all = clients
