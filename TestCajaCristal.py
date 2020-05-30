import unittest

def es_mayor_de_edad(edad):
        if edad >= 18:
            return True
        else:
            return False

class MyTest(unittest.TestCase):
    
    def test_mayor_de_edad(self):
        edad = 21
        
        resultado = es_mayor_de_edad(edad)
        
        self.assertTrue(resultado)
    
    def test_menor_de_edad(self):
        edad = 15
        
        resultado = es_mayor_de_edad(edad)
        
        self.assertFalse(resultado)
        


if __name__ == '__main__':
    unittest.main()