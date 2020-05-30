import unittest

def suma(numero_1, numero_2):
        return numero_1 + numero_2

class MyTest(unittest.TestCase):
    
    def test_suma_dos_positivos(self):
        numero_1 = 10
        numero_2 = 15
        self.assertEqual(suma(numero_1, numero_2), 25)
    
    def test_suma_dos_negativos(self):
        numero_1 = -10
        numero_2 = -15
        self.assertEqual(suma(numero_1, numero_2), -25)
        


if __name__ == '__main__':
    unittest.main()