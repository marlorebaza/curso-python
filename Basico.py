import collections
import random


if __name__ == '__main__':
    '''
        Operadores matematicos
    '''
    # suma
    print(1 + 1) # 2
    # resta 
    print(10 - 1) # 9 
    # multiplicacion
    print(10 * 2)  # 20
    # division
    print(11 / 4) # 2.75
    # division de enteros (excluye decimales)
    print(11 // 4) # 2 
    # residuo
    print(3 % 2) # 1
    # exponencia
    print(2**3) # 8
    
    # Es posible multiplicar una cadena
    print('hola' * 5) # holaholaholaholahola
    
    
'''
    Convenciones:
    - las palabras dentro del nombre de las variables y funciones se separan con guiones bajos
    - dejar 2 saltos de línea despues de bloques de código
    - el nombre de las constantes se escriben con mayuscula
    - el nombre de las variables / funciones privadas deben comenzar con un guión bajo: _value
    - el nombre de las variables / funciones que no deben ser modificadas deben comenzar con doble guión bajo: __value
'''
    
'''
    palabra clave global:
    Permite modificar una variable fuera del ambito actual. Es usada para crear o modificar una variable global
    desde un ambito no global. Por ejemplo: desde una función
    FUENTE: https://www.geeksforgeeks.org/global-keyword-in-python/
'''
variable_global = 'hola'
def set_variable_global():
    global variable_global
    variable_global += ' marlo'
    
    
def show_variable_global():
    print(variable_global)
    
    
set_variable_global()
show_variable_global()


'''
    Python reusa los espacios en memoria si los valores coinciden
'''
cadena = 'Peru'
# id: función que devuelve la dirección en memoria de una variable / objeto 
print(id(cadena) == id('Peru')) # True
# como era de esperar los caracteres con tilde o mayuscula / minuscula no son considerados iguales
print(id('u') == id('ú')) # False
print(id('u') == id(cadena[-1])) # True
# las cadenas son inmutables. Para comprobarlo adicionamos caracteres a la variable "cadena",
# luego de esto su dirección en memoria ya no será la misma, python le asignará otra.
# Estos debido a que python reusa el espacio en memoria y dado que podría estar siendo referenciado por otras variables
# decide no trabajar sobre el mismo espacio.
cadena += "anos"
print(id(cadena) == id('Peru')) # False


def my_function():
    ''' Documentación de esta función...  '''
    pass

# jelp: proporciona un mensaje informativo del objeto enviado
help(my_function)
help(dir)

## dir: retorna una lista con los atributos (propiedades y funciones) del objeto
print(dir(cadena))


''' 
Slices (rebanadas):
cadena[inicio:final:pasos]
- inicio x defecto es 0
- final (no incluido), x defecto es la longitud
- pasos x defecto es 1, si es negativo comienza desde el final hacia la izquierda
'''
my_value = "vamos Perú!"
print(my_value[:]) # vamos Perú!
print(my_value[:3:-1]) #úreP s
print(my_value[2::2]) # msPr!


'''
Iteradores:
'''
def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b
        
iterable1 = fibonacci(20)

# iteramos generador
print([num for num in iterable1])

# una vez que la iteración sobre un generador ha terminado, ya no podemos utilizarlo
print([num for num in iterable1]) # ya no retornará nada
print([num for num in fibonacci(30)]) # creamos un nuevo iterable

'''
Listas:
'''
# Concatenación de listas
list1 = [1, 2, 3, 4, 5]
list2 = list(range(6, 11))
print(list1 + list2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# multiplicacion de listas
print(list1 * 3) # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# filtrar:
# - filter(funcion, iterable): retorna un iterador sobre los elementos que coincidan con la funcion enviada
list3 = ['mazio', 'pele', 'lolo', 'malo']
filterList3 = filter(lambda e: e.startswith('ma'), list3)
# - next(iterable, por_defecto): retorna el elemento siguiente del iterable. Si se proporciona un valor por_defecto
# se devolverá este valor, en lugar de un StopIteration cuando se haya terminado la iteración
print('resultado: {}'.format(next(filterList3, None))) # mazio


'''
Diccionarios
'''
dict1 = {'age': 29, 'name': 'ronaldo', 'nationality': 'brasilian'}
# llaves
for key in dict1.keys():
    print(key)
    
# valores
for value in dict1.values():
    print(value)
    
# elemento completo
for key, value in dict1.items():
    print('{}: {}'.format(value, key))
    
# si se quiere obtener un valor con una llave inexiste, se arrojará una excepción
#print(dict1['noExisto'])

# mejor es obtenerla de esta forma para poder controlar
print(dict1.get('noExisto', 'no existo, pero tengo este valor x defecto :)'))

# update(): agrega las llaves y valores. En caso ya existan las llaves, reemplaza los valores
dict1.update({'name': 'pele', 'age': 71, 'goals': 1500})
print(dict1)

# Creamos nuestro diccionario personalizado
class MyDictionary(collections.UserDict):
    # sobre-escribimos el método __getitem__ y prefijamos "my-dictionary: " al valor que se queira obtener
    def __getitem__(self, key):
        return 'my-dictionary: ' + super().__getitem__(key)

myDictionary = MyDictionary({"name": "marlo", "age": 29})
print(type(myDictionary)) # <class '__main__.MyDictionary'>
print(myDictionary["name"]) # my-dictionary: marlo

'''
Tuplas:
- Son inmutables: no permite agregar valores ni modificar los ya existentes
'''
tuple1 = (1, 2, 3)
# lista a tupla
tuple1 = tuple([1, 2, 3])
print(type(tuple1))
#tuple1[0] = 10 # esto genera un error
print(tuple1[0])
# solamente cuenta con los métodos publicos index() y count()
print(dir(tuple1))

# collections.namedtuple(nombre_sub_clase, nombre_campos): Crea una sub clase de tupla con campos nombraados
Months = collections.namedtuple('Meses', ('Enero', 'Febrero', 'Marzo'))
print(type(Months)) # <class 'tuple'>
# Creamos una instancia de nuestra tupla Months, enviándole en su constructor los valores de los campos definidos
months = Months(1, 2, 3)
# De esta forma  podremos obtener los valores de la tupla a traves de nombres (y ya no de indices)
print(months.Enero) # equivalencia: months[0]
print(months.Febrero) # equivalencia: months[1]
print(months.Marzo) # equivalencia: months[2]

'''
Conjuntos
- No mantienen un orden
- No guardan valores repetidos
'''
set1 = {1, 2, 3, 4, 5}
set2 = set([5, 6, 7, 8, 9])
set1.add(1) # no agregarà el 1 xk ya existe en set1
set2.add(10)
# print(set1[-1]) # esto genera un error, ya que los set no soportan indexado
# operaciones con conjuntos
print(set1.union(set2)) # todos los elementos: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(set1.intersection(set2)) # elementos en comun: {5}
print(set1.difference(set2)) # elementos de set1 que no existen en set2: {1, 2, 3, 4}


'''
Comprenhensions
'''
numbers = list(range(100))
# comprenhension list de números impares
odd_numbers = [number for number in numbers if number % 2 != 0]
print(odd_numbers)
# comprenhension diccionario
names = ['marlo', 'pele', 'ronaldo']
uids = [1, 2, 3]
# zip(iterable1, iterable2, iterable3,...):
# retorna un "zip object", cuyo método __next__() returna una tupla con los elementos por cada posición de los
# iterables enviados. Esta iteración continuará hasta que el iterable mas pequeño se haya recorrido
uids_and_names = {uid: name for uid, name in zip(uids, names)}
print(uids_and_names) # {1: 'marlo', 2: 'pele', 3: 'ronaldo'}
# comprenhension conjunto.
# random.randint(min, max): retorna un número aleatorio entre el rango (ambos valores están incluidos)
repeated_numbers = [random.randint(1, 3) for number in range(100)]
non_repeated_numbers = {number for number in repeated_numbers}
print(non_repeated_numbers)
