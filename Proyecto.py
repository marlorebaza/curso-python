import sys

clients = [
        {
            'name': 'Ricardo',
            'company': 'Google',
            'email': 'ricardo@google.com',
            'position': 'Master'
        },
        {
            'name': 'Pablo',
            'company': 'Mocosoft',
            'email': 'pablo@mocosoft.com',
            'position': 'Developer'
        }
    ]

def create_client(client):
    global clients
    
    if client['name'] not in clients:
        clients.append(client)
    else:
        # escapamos comilla dentro de cadena anteponiendo back-slash
        print('Client already is in the client\'s list')
    
    
def list_clients():
    global clients
    
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
    _print_welcome()
    
    command = input().upper()
    
    if command == 'C':
        create_client({
            'name': _get_field_value_of('name'),
            'company': _get_field_value_of('company'),
            'email': _get_field_value_of('email'),
            'position': _get_field_value_of('position')
        })
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'D':
        delete_client(_get_client_name())
        list_clients()
    elif command == 'U':
        update_client(
            _get_client_name(),
            {
                'name': _get_field_value_of('name'),
                'company': _get_field_value_of('company'),
                'email': _get_field_value_of('email'),
                'position': _get_field_value_of('position')
            })
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found_client = search_client(client_name)
        if found_client:
            print('The client is in the clients list')
        else:
            print('The client: \'{}\' is not in the client list'.format(client_name))
            
    else:
        print('Invalid command') 
    
'''
    AVERIGUAR E IMPLEMENTAR INTERNALIZACION 
    ACA ME QUEDO:
    https://platzi.com/clases/1378-python-practico/14172-python-comprehensions/
'''
    
