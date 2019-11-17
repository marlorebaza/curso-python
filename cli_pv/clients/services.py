import csv
import os

from clients.models import Client

from builtins import vars

class ClientService:
    
    def __init__(self, table_name):
        self.table_name = table_name
        
        
    def create_client(self, client):
        with open(self.table_name, mode='a') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict())
        
        
    def list_clients(self):
        with open(self.table_name, mode='r') as f:
            reader = csv.DictReader(f, fieldnames=Client.schema())
            return list(reader)
        
    def update_client(self, updated_client):
        clients = self.list_clients()
        client = self._get_client(clients, updated_client.uid)
        if client:
            client.update(updated_client.to_dict())
        self._save_to_disk(clients)
    
    '''
    def delete_client(self, client_uid):
        clients = self.list_clients()
        client = self._get_client(clients, client_uid)
        if client:
            clients.remove(client)
            self._save_to_disk(clients)
    '''
        
    def delete_client(self, client):
        clients = self.list_clients()
        clients.remove(client)
        self._save_to_disk(clients)
        
    def _get_client(self, clients, client_uid):
        return next(filter(lambda c: c['uid'] == client_uid, clients), None)
        
    def _save_to_disk(self, clients):
        tmp_table_name = self.table_name + '.tmp'
        with open(tmp_table_name, mode = 'w') as f:
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerows(clients)
            
        os.remove(self.table_name)
        os.rename(tmp_table_name, self.table_name)
                