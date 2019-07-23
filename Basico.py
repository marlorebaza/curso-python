

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
