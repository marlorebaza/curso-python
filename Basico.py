import collections
import random
import os
from contextlib import contextmanager
from pip._vendor.idna.core import valid_contexto
from functools import update_wrapper


'''
Sobre los PEP's (python enhancement proposal): 

FUENTE: https://www.python.org/dev/peps/

Describen cambios al lenguaje o a los estándares alrededor.


Los principales:

- PEP8: Python style guide
- PEP257: Python docstrings (sobre como se debe documentar)
- PEP20: Como un resumen de buenas practicas. Se puede ver ejecutando: import this

Info de esto en platzi:
https://platzi.com/clases/1378-python-practico/14191-python-2-vs-3-y-cierre-del-curso/
'''

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

'''
Busqueda binaria
'''
def binary_search(iterable, target, min_index, max_index):

    if min_index > max_index:
        return False
    
    # division de enteros, sin tomar decimales
    mid = (min_index + max_index) // 2 
    
    if target == iterable[mid]:
        return True
    elif target < iterable[mid]:
        return binary_search(iterable, target, min_index, mid - 1)
    else:
        return binary_search(iterable, target, mid + 1, max_index)
    
    
    '''
    # Sin recursividad
    mid = -1
    while min_index <= max_index:
        
        mid = (min_index + max_index) // 2
    
        if target == iterable[mid]:
            return True
        elif target < iterable[mid]:
            max_index = mid - 1
        else:
            min_index = mid + 1
            
    return False
    '''

numbers = [random.randint(0, 100) for _ in range(10)]
numbers.sort()
print (numbers)
#target = int(input('¿Qué número deseas buscar?'))
target = 88
found = binary_search(numbers, target, 0, len(numbers) - 1)
print(found)


'''
*args Y **kwargs:
- *args: captura las variables no nombradas en una tupla.
- **kwargs: captura las variables nombradas en un diccionario.
NOTA: al llamar a una función, los parametros nombrados se deden enviar al final 
'''

def my_function(some_number, some_string, *arguments, **keyworded_arguments):
    print('some_number = {} de tipo {}'.format(some_number, type(some_number)))
    print('some_string = {} de tipo {}'.format(some_string, type(some_string)))
    print('arguments = {} de tipo {}'.format(arguments, type(arguments)))
    print('keyworded_arguments = {} de tipo {}'.format(keyworded_arguments, type(keyworded_arguments)))

my_function(123, 'hi!', True, 12322, ':D', another_boolean=False, another_string = "12das", another_number = 123)
# Resultado:
#some_number = 123 de tipo <class 'int'>
#some_string = hi! de tipo <class 'str'>
#arguments = (True, 12322, ':D') de tipo <class 'tuple'>
#keyworded_arguments = {'another_boolean': False, 'another_string': '12das', 'another_number': 123} de tipo <class 'dict'>


'''
Decoradores: son una función que envuelve a otra función para modificar o extender su comportamiento.
En Python las funciones pueden recibir funciones como parámetros y pueden regresar funciones. 
Los decoradores utilizan este concepto de manera fundamental.
'''
# Definimos un decorador que convierte a mayusculas el resultado de una función
def to_upper(func):
    print('dentro de decorator')
    # capturamos los parametros recibidos y los pasamos tal cual a la función que se está invocando
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs).upper()
        return result
    
    return wrapper

# Para usar un decorador sobre una funcióm, prefijamos el simbolo arroba (@) al nombre del decorador y lo ponemos
# sobre la funcion
@to_upper
def say_hello(value):
    return 'Hola {}'.format(value)

print('Se va a ejecutar say_hello(...)')
print(say_hello('marlo'))

# Decorador con parámetros
def repeat(times = 5):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            # iteramos times y llamamos a la funcion decorada
            for _ in range(times):
                fn(*args, **kwargs)
        # retornamos la función wrapper
        return wrapper
    # retornamos el decorador
    return decorator

# repeat(10) invocará a la función "repeat" que devuelve un decorador 
@repeat(10)    
def perform(value):
    print(value)
    
# Dado que la función "repeat" no es un decorador en sí (ya que el decorador lo retorna adentro), se debe indicar
# con parentesis como una función normal
@repeat()
def perform2(value):
    print(value)
    
perform("Hola soy marlo")
perform2('Hola causa')

# Multiples decoradores a una función: los decoradores se ejecutaán de adentro hacia afuera
def add_preffix(fn):
    def wrapper(*args, **kwargs):
        return "O_O - " + fn(*args, **kwargs)
    
    return wrapper

# primero se ejecutrá "add_preffix" y luego "to_upper"
@to_upper
@add_preffix
def gretting_in_spanish(name):
    return "Hola humano %s" % name

print(gretting_in_spanish("Marlo"))


'''
Clases:
- En python solamente es posible definir un unico constructor (__init__),
ya que python no soporta la sobrecarga de métodos.
Si en algo ayuda es posible definir un valor x defecto a un parámetro con el signo igual:
'def method(p2, p1 = None):...', de esta manera no es necesario que se envíe cuando se llama a la función:
'method(12)'
'''    
class Person:
    
    # __new__(...): función llamada primera, antes que __init__, 
    # y es responsable de retornar una nueva instancia de la clase
    # Recibe como parámetro la clase actual
    def __new__(cls, name, age):
        print('inside of Person.__new__(...)')
        if cls == Student:
            print('se esá creando un estudiante')
            # super(): hace referencia al objeto padre, en este caso sería object
            return super(Person, cls).__new__(cls)
        else:
            print('NO se esá creando un estudiante, se forzará la creación de uno >:)')
            return Student(name, age)
    
    # __init__(...): inicializa un objeto de la clase
    def __init__(self, name, age, email = None):
        print('inside of Person.__init__(name, age, email)')
        self.name= name
        self.age = age
        self.email = email
        # por convención las variables privadas se nombran con un guion bajo inicial. 
        self._dont_use_me = ':D'
        
    def say_hello(self):
        print('Hola mi nombre es {} y tengo {} años.'.format(self.name, self.age))
        
# Indicamos la clase base entre parentesis (herencia).
# Object es la clase base x defecto, Desde python 3 'class Person:' es equivalente a
# 'class Person(Object):'
class Student(Person):
    
    def __init__(self, name, age):
        print('inside of Student.__init__(...)')
        super(Student, self).__init__(name, age)
        
class Teacher(Person):
    
    def __init__(self, name, age):
        print('inside of Teacher.__init__(...)')
        super(Student, self).__init__(name, age)

student1 = Student('marlo', 29)
student1.say_hello()
# no deberían usarse las variables privadas, aunque tecnicamente sea posible
print(student1._dont_use_me)
print ('-------------------')
teacher1 = Teacher('lula', 31)
teacher1.say_hello()

'''
Patron singleton
'''
class MySingleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        print('inside of MySingleton.__new__(...)')
        # 'cls._instance' es equivalente a 'MySingleton._instance'
        if not cls._instance:
            cls._instance = super(MySingleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance
mySingleton1 = MySingleton();
mySingleton2 = MySingleton();
mySingleton3 = MySingleton();
mySingleton4 = MySingleton();
print(id(mySingleton1) == id(mySingleton2) == id(mySingleton3) == id(mySingleton4)) # True
# Mas info sobre __new__:
# https://howto.lintel.in/python-__new__-magic-method-explained/

# @classmethod vs @staticmethod
class MyClass:
    
    # En python todas las variables a nivel de clase son consideradas estátics
    im_static = 'Hi'
    
    def __init__(self, name):
        self.name = name
    
    # Método de instancia: Solamente puede ser llamado desde una instancia de la clase.
    # Recibe implicitamente la instancia como primer parámetro
    def say_hi(self):
        print ('Hi %s' % self.name)
        
    # Método de clase: la clase del objeto es enviada implicitamente como primer parámetro.
    # Puede ser llamado desde una instancia o anteponiendo la clase directamente
    @classmethod
    def createInstance(cls, name):
        print(cls)
        return cls(name)
    
    # Método estatico: no recibe ni la clase, ni la instancia.
    # Puede ser llamado desde una instancia o anteponiendo la clase directamente
    @staticmethod
    def execute_say_hi(instance):
        instance.say_hi()
        
myClass1 = MyClass('Marlo')
myClass1.say_hi()

myClass2 = myClass1.createInstance('Marlo')
myClass3 = MyClass.createInstance('Marlo')

MyClass.execute_say_hi(myClass2)
MyClass.execute_say_hi(myClass3)

# al crearse una instancia de una clase, las variables que tenga definidias a nivel de clase 
# se crearán dentro de esta instancia y ya no serán las mismas que las de la1 clase en si misma. Ejemplo
MyClass.im_static = ':D'
myClass1.im_static = 'MARLO'
print (MyClass.im_static == myClass1.im_static) # False

'''
Scope: es la parte del programa en el que podemos tener acceso a un namespace sin necesidad de prefijos.
En cualquier momento determinado, el programa tiene acceso a tres scopes:
1. El scope dentro de una función (que tiene nombres locales)
2. El scope del módulo (que tiene nombres globales)
3. El scope raíz (que tiene los built-in names)
Cuando anidamos una función dentro de otra función, su scope también queda anidado dentro del scope de la función padre.
'''
global_variable = 10
def returnFunction(parent_local_variable):
    another_parent_local_variable = 20
    def inside(local_variable):
        # Para poder manipular una variable que se encuentra fuera del scope local podemos utilizar los keywords:
        # - global: variable creada a nivel de módulo
        # - nonlocal: variable creada a nivel de función (en una función padre).
        # Si no se hiciese uso de estas palabras claves entonces se crearían nuevas variables locales con esos nombres
        nonlocal another_parent_local_variable
        another_parent_local_variable = 100
        global global_variable
        global_variable = 50
        # podemos acceder al scope global (modulo), de la función padre y al propio scope de la función
        print(local_variable + parent_local_variable + global_variable)
    return inside

plus = returnFunction(35) 
# Al llamar a la función "plus", esta podrá acceder al scope de su función padre, dando como resultado:
# local_variable = 10 + parent_local_variable = 35 + global_variable = 50
plus(10) # 95
# comprobamos el cambio de valor de la variable global
print(global_variable) # 50



'''
Emulando Framework click

'''
class ClickContext:
    # sobreescribimos este método para poder crear los atributos que no existan y evitar un error
    # para esta pequeña emulación todos los atributos se crearán como diccionarios
    def __getattribute__(self, name):
        try:
            return object.__getattribute__(self, name)
        except AttributeError:
            return {}
    
context = ClickContext()

def get_current_context():
    return context
    
class Group:
    
    def __init__(self):
        self._commands = []
    
    def get_commands(self):
        return self._commands
    
    def command(self):
        def decorator(fn):
            self._commands.append(fn)
        return decorator
    
    def add_commands(self, commands):
        self._commands.append(commands)
        

def group():
    def decorator(fn):
        #desc = help(fn)
        group = Group()
        fn()
        return group
    return decorator

def option(*args, **kwargs):
    def decorator(fn):
        # haz algo con los parámetros externos e internos...
        #print('wrapper pa %s'  % fn)
        if not hasattr(fn, '__options__'):
            fn.__options__ = []
        # hacemos un "prepend", es decir agregamos al inicio, ya que los decoradores se ejeutan de adentro hacia afuera.
        # De esta forma alineamos los decoradores de abajo hacia arriba con respecto a los parámetros de la 
        # funcion en cuestion
        fn.__options__ = [(args, kwargs)] + fn.__options__
        #fn.__options__.insert(0,(args, kwargs))
        return fn
    return decorator

def pass_context(fn):
    def new_func(*args, **kwargs):
        return fn(get_current_context(), *args, **kwargs)
    '''
    Sobre: update_wrapper(funcion_envoltura, funcion_a_envolver[, atributos_a_asignar, atributos_a_actualizar])
    La funcion_envoltura será actualizada con los atributos_a_asignar (seteo) y 
    atributos_a_actualizar (el atributo debe ser un diccionario para poder hacer uso de su método update(). 
    Por ejemplo: __dict__) de la funcion_a_envolver.
    Finalmente se agregará la funcion_a_envolver en el atributo '__wrapped__' de la funcion_envoltura
    y la funcion_envoltura será retornada
    '''
    # Ahora la nueva función envolverá a la función real y cuando sea invocada le pasará como primer parámetro
    # el contexto actual y luego el resto de parámetros que reciba
    return update_wrapper(new_func, fn)

# Bloque 1 (emula a clients/commands.py)

@group()
def persons():
    """Manage Persons"""

@persons.command()
@option('-n', '--name')
@option('-a', '--age')
@pass_context
def create(ctx, name, age):
    print('ejecutando create. argumentos recibidos ctx.obj[''nombre_tabla''] = {ctx}, name = {name} y age = {age}'
          .format(ctx=ctx.obj['nombre_tabla'], name=name, age=age))
    
@persons.command()
@pass_context
def list(ctx):
    print('ejecutando list. argumentos recibidos ctx.obj[''nombre_tabla''] = {}'.format(ctx.obj['nombre_tabla']))
    
all = persons

# Bloque 2 (emula a pv.py)

@group()
@pass_context
def cli(ctx):
    ctx.obj = {'nombre_tabla': '.cliente.csv'}

cli.add_commands(all)

def analize(group):
    for command in group.get_commands():
        if type(command) == Group:
            print('analizando grupo')
            analize(command)
        else:
            print('se va a ejecutar %s' % command.__name__)
            if hasattr(command, '__options__'):
                # deberían haber tantas opciones como parámetros definidos en la función (para esta pequeña logica)
                # estoy pasando de frente todas las opciones sin descomponer la data dentro de cada una que la librería
                # Click si lo hace para mostrar un input, un label, validación, etc... 
                command(*command.__options__)
            else:
                command()
            
analize(cli)


'''
Gestion de excepciones
'''
# bloque try:
try:
    number = int('NO SOU NUMERO')
except ValueError:
    # controla la excepción ValueError
    print('Error: Número incorrecto')
except:
    # controla el resto excepciones
    print('Algún error ocurrió')
else:
    # este bloque se ejecutará si no hubo errores lanzados
    print('No hubo errores')
finally:
    # este bloque se ejecutará siempre
    print('No me importa si hubo o no errores...')
    
# custom exception
class MyException(BaseException):
    pass

def testMyException(value):
    if value < 0:
        raise MyException('Valor incorrecto')
    else:
        print('good!')

testMyException(10) # good!
try:
    testMyException(-1)
except MyException as e:
    print(str(e)) # Valor incorrecto
    
    
'''
get / set atributos
'''
def iAmAnExample():
    pass
# setea el nombre del atributo, sobre el objeto indicado, con el valor especificado
# equivalente a: iAmAnExample.__nuevo__ = ':D'
setattr(iAmAnExample, '__nuevo__', ':D')
# obtiene el valor del atributo del objeto indicado
# equivalente a: iAmAnExample.__module__
print(getattr(iAmAnExample, '__module__'))
print(getattr(iAmAnExample, '__nuevo__'))
# si el atributo no existe se lanzará una excepción, para evitar esto se debe indicar el valor x defecto como 3er parámetro
print(getattr(iAmAnExample, '__noExisto__', 'D:'))
    
    
'''
with:
Se usa para envolver la ejecución de un bloque con métodos definidos por un gestor de contexto (context manager).

Un context manager es un objeto que define el contexto a ser establecido en tiempo de ejecución cuando se ejecuta una
sentencia "with". El context manager maneja la "entrada a" y la "salida de" deseados para la ejecución del bloque de
codigo.
Los context manager son normalmente invocados usando la sentencia "with", pero también puedes ser usados invocando
directamente a sus metodos.
Los usos tipicos de un context manager son para guardar o restaurar varios tipos de estados globales, abrir o cerrar
recursos, abrir o cerrar archivos, etc

Mas información sobre tipos de contexts managers en https://docs.python.org/2/library/stdtypes.html#typecontextmanager

Info en platzi: https://platzi.com/clases/1378-python-practico/14337-context-managers/
'''
class MyWith:
    # Método de entrada al contexto, en tiempo de ejecución, relacionado con este objeto.
    # La sentencia "with" vinculará lo retornado por este método a la variable indicada en la clausula "as" 
    # en caso haya una. Es retorno es opcional.
    def __enter__(self):
        print('dentro de __enter__')
        return 'Hola!'
    
    # Método de salida del contexto, en tiempo de ejecución, relacionado con este objeto.
    # Parámetros:
    # - exc_type: clase de la excepción que provocó la salida del contexto
    # - exc_value: mensaje de la excepción que provocó la salida del contexto
    # - traceback: rastreo de pila de la excepción que provocó la salida del contexto
    def __exit__(self, exc_type, exc_value, traceback):
        print('dentro de __exit__ - argumentos: exc_type = %s, exc_value = %s y traceback = %s' 
              % (exc_type, exc_value, traceback))
        # si se recibe una excepción y se quiere evitar que se propague se debe retornar un valor verdadero,
        # de lo contrario, la excepción se procesará normalmente al salir de este método.
        return True

# Asignamos lo retornado por el método "__enter__" a la variable "mw"
with MyWith() as mw:
    print(mw) # Hola!
    
# No es necesario envolver el bloque with para controlar la excepción, ya que en el método "__exit__" 
# se evita la propagación retornando True
with MyWith() as mw:
    raise Exception('Error!!')
    
# creamos una instancia de la clase
mw = MyWith()
print('antes de segundo with')
with mw:
    # dado que no hacemos uso de "as", la variable mw será una instancia de la clase "MyWith"
    print(mw) # <__main__.MyWith object at XXXXX>
    
# NOTA: en una ejecución de más de un item a la vez, los context managers son procesados como si multiples sentencias "with"
# estuvieran enlazadas. Ejemplo
'''
with A() as a, B() as b:
    pass
# Es equivalente a:
with A() as a:
    with B() as b:
        pass
'''
    
'''
Decorador @contextmanager:
este decorador permite definir una función fábrica para gestionar contextos con la sentencia "with", sin la 
necesidad de crear una clase o métodos separados "__enter__()" y "__exit__()"
'''
@contextmanager
def myContextManager():
    try:
        print('dentro de try')
        # Cuando la función cede (yields), el bloque dentro de "with" es ejecutado. En caso se ceda un valor 
        # este se asignará a la variable indicada en la sentencia "as" en "with".
        # Luego de salir del bloque "with", se reanuda la ejecución de esta función en el punto donde se cedió.
        # En caso se genere una excepción no controlada en el bloque "with", se vuelve a generar en este punto
        # la misma excepción. Es por esto que podemos controlarla en el bloque "except"
        print('antes de yield')
        yield "Hola!"
        print('despues de yield')
    except:
        # Capturaremos cualquier excepción surgida en el bloque dentro de "with". En caso querramos evitar
        # su propagacón no relazamos la excepción
        print('dentro de except')
        # Si no se indica una expresión en "raise" entoces se re-lanzará la última excepción activa en el scope actual.
        # si no hay una excepción activa en el scope actual, entonces se arrojará la excepción TypeError.
        # Comentamos raise
        #raise
        # Este bloque es equivalente a:
        #except Exception as e:
        #   raise e
    else:
        print('dentro de else')
        pass
    finally:
        print('dentro de finally')
        pass

with myContextManager() as mcm:
    print(mcm) # Hola!
    
with myContextManager() as mcm:
    raise Exception('Error!!')
    
mcm = myContextManager()
print('antes de segundo with')
with mcm:
    print(mcm) # <__main__.MyWith object at XXXXX>
    
    
'''
    Formateo literal de cadena
    La cadena debe ser precedida por el caracter "f"
    FUENTE: https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
'''
some_number = 12
some_string = 'Marlo'
print(f'Hola {"soy"} {some_string} y tengo {some_number} años')


'''
    Variables de entorno
'''
# Obtener un diccionario con todas las variables de entorno
print(os.environ)
# Obtener el valor de una variable
print(os.environ.get('PATH'))
print(os.environ['PATH'])
# Agregar una variable
os.environ['PRUEBA_A'] = 'ASDASDAS'
os.environ.setdefault('PRUEBA_B', 'zcxzxczc')


'''
    Archivo __init__.py
    - Son requeridos para que python trate al directorio como paquete y lo hace "importable". 
    Este archivo en principio puede estar vacío, pero tambien puede ejecutar código de inicialización para el paquete.
    FUENTEs:https://docs.python.org/3/tutorial/modules.html#packages
    - Desde la version 3.3 ya no es requerido, ya que los paquetes tienen un espacio de nombres implicito. 
    FUENTE: https://stackoverflow.com/questions/37139786/is-init-py-not-required-for-packages-in-python-3-3
'''
# Ejemplo de como podemos aprovechar el archivo __init__.py
# FUENTE: https://stackoverflow.com/a/29509611

# Dado que en __init__.py hemos importado el contenido de todos lo modulos dentro del paquete init_use,
# importamos la función do_something sin indicar el módulo que la contiene:
#from init_use.file1 import do_something
from init_use import do_something
do_something()
    


'''
    AVERIGUAR E IMPLEMENTAR INTERNALIZACION 
    
    AHORA SI!: https://platzi.com/clases/1378-python-practico/14186-actualizacion-de-cliente/
'''


