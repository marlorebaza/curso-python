clients = 'pablo,ricardo,'

def create_client(client_name):
    global clients
    
    if client_name not in clients:
        clients += client_name
        _add_coma()
    else:
        # escapamos comilla dentro de cadena anteponiendo back-slash
        print('Client already is in the client\'s list')
    
    
def list_clients():
    global clients
    
    print(clients)
    
    
def update_client(client_name, updated_client_name):
    global clients
    
    if client_name in clients:
        clients = clients.replace(client_name, updated_client_name)
    else:
        print('Client ''{}'' is not in the client list'.format(client_name))
        
def delete_client(client_name):
    global clients
    
    if client_name in clients:
        clients = clients.replace('{},'.format(client_name), '')
    else:
        print('Client ''{}'' is not in the client list'.format(client_name))
    
    
def _add_coma():
    global clients
    
    clients += ','
    
def _get_client_name(message = 'What is the client name?'):
    return input(message)
    
    
def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 5)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')


if __name__ == '__main__':
    _print_welcome()
    
    command = input().upper()
    
    if command == 'C':
        create_client(_get_client_name())
        list_clients()
    elif command == 'D':
        delete_client(_get_client_name())
        list_clients()
    elif command == 'U':
        update_client(_get_client_name(), _get_client_name('What is the updated client name?'))
        list_clients()
    else:
        print('Invalid command') 
    
'''
    AVERIGUAR E IMPLEMENTAR INTERNALIZACION 
    ACA ME QUEDO:
    https://platzi.com/clases/1378-python/14096-for-loops/
'''
    
