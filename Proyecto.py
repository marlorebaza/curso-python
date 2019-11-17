import sys
import csv
import os

clients = []
# el '.' como prefijo del nombre del archivo indica que debe ser tr
CLIENT_FILE_NAME = '.clients.csv'
CLIENT_SCHEMA = ['uid', 'name', 'company', 'email', 'position']

def _initialize_clients_from_storage():
    # open(): Abre un archivo. por defectto el modo en el que se abre es lectura (r)
    # en modo lectura el archivo debe existir, sino arrojará la excepción: 
    # FileNotFoundError: [Errno 2] No such file or directory
    with open(CLIENT_FILE_NAME) as f:
        reader = csv.DictReader(f, CLIENT_SCHEMA)
        for row in reader:
            clients.append(row)

def _save_clients_from_storage():
    client_temp_file_name = '{}.tmp'.format(CLIENT_FILE_NAME)
    with open(client_temp_file_name, mode = 'w') as f:
        writer = csv.DictWriter(f, CLIENT_SCHEMA)
        writer.writerows(clients)

    os.remove(CLIENT_FILE_NAME)
    os.rename(client_temp_file_name, CLIENT_FILE_NAME)

def create_client(client):
    global clients
    
    if client['name'] not in clients:
        clients.append(client)
    else:
        # escapamos comilla dentro de cadena anteponiendo back-slash
        print('Client already is in the client\'s list')
    
    
def list_clients():
    global clients
    
    print('uid | name | company | email | position')
    print('****************************************')
    
    # enumerate(): retorna un enumerador con el indice y el valor del elemento
    for index, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = index,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))
    
def search_client(client_name):
    for current_client in clients:
        if client_name == current_client['name']:
            return True
    return False
    
    
def update_client(client_name, updated_client):
    global clients
    
    client = _get_client(client_name)
    
    if client:
        client.update(updated_client)
        
def delete_client(client_name):
    global clients
    
    client = _get_client(client_name)
    
    if client:
        # remove(): elimina el primer elemento coincidente
        clients.remove(client)
        
def _get_client(client_name):
    
    client = next(filter(lambda c: client_name.upper() == c['name'].upper(), clients), None)
    
    if not client:
        print('Client ''{}'' is not in the client list'.format(client_name))
        
    return client
    
    
def _get_field_value_of(field_name):
    field_value = None
    
    while not field_value:
        field_value = input('What is the client {}?'.format(field_name))
    
    return field_value
    
    
def _get_client_name(message = 'What is the client name?'):
    client_name = None
    
    while not client_name:
        client_name = input(message)
        if client_name == 'exit':
            client_name = None
            break
        
    if not client_name:
        sys.exit()
    return client_name
    
    
def _print_welcome():
    
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 5)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')


if __name__ == '__main__':
    
    _initialize_clients_from_storage()
    
    _print_welcome()
    
    command = input().upper()
    
    if command == 'C':
        create_client({
            'name': _get_field_value_of('name'),
            'company': _get_field_value_of('company'),
            'email': _get_field_value_of('email'),
            'position': _get_field_value_of('position')
        })
    elif command == 'L':
        list_clients()
    elif command == 'D':
        delete_client(_get_client_name())
    elif command == 'U':
        update_client(
            _get_client_name(),
            {
                'name': _get_field_value_of('name'),
                'company': _get_field_value_of('company'),
                'email': _get_field_value_of('email'),
                'position': _get_field_value_of('position')
            })
    elif command == 'S':
        client_name = _get_client_name()
        found_client = search_client(client_name)
        if found_client:
            print('The client is in the clients list')
        else:
            print('The client: \'{}\' is not in the client list'.format(client_name))
            
    else:
        print('Invalid command') 
        
    
    _save_clients_from_storage()
   
    
