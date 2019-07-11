

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

# ACA ME QUEDO: https://platzi.com/clases/1378-python/14089-operadores-logicos/

