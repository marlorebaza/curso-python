import uuid

class Client:
    
    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        # uuid: este modulo proporciona objetos UUID inmutables 
        # uuid.uuid4(): genera un UUID aleatorio
        # FUENTE: https://docs.python.org/3/library/uuid.html
        self.uid = uid or uuid.uuid4()
        
    def to_dict(self):
        # vars(object): retorna el valor del atributo "__dict__" del objeto enviado.
        # si el objeto enviado no tiene ese atributo arrojará una excepción TypeError.
        # "vars(self)" es equivalente a "self.__dict__"
        return vars(self)
    
    @staticmethod
    def schema():
        return ['name', 'company', 'email', 'position', 'uid']
    
    
if __name__ == '__main__':
    print (uuid.uuid4())