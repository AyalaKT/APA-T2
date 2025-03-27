"""
primos.py

Autor: [Tu Nombre]

Este módulo proporciona funciones para trabajar con números primos,
incluyendo verificación de primalidad, generación de números primos,
descomposición en factores primos, y cálculo de MCD y MCM.

Incluye tests unitarios para cada función.
"""
import math
from functools import reduce

def esPrimo(numero):
    """Devuelve True si el número es primo, False en caso contrario."""
    if numero < 2:
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return False
    return True

def primos(numero):
    """Devuelve una tupla con los números primos menores que el argumento."""
    return tuple(n for n in range(2, numero) if esPrimo(n))

def descompon(numero):
    """Devuelve una tupla con la descomposición en factores primos del argumento."""
    factores = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores.append(divisor)
            numero //= divisor
        divisor += 1
    return tuple(factores)

def mcm(num1, num2):
    """Devuelve el mínimo común múltiplo de dos números."""
    return abs(num1 * num2) // math.gcd(num1, num2)

def mcd(num1, num2):
    """Devuelve el máximo común divisor de dos números."""
    return math.gcd(num1, num2)

def mcmN(*numeros):
    """Devuelve el mínimo común múltiplo de varios números."""
    return reduce(mcm, numeros)

def mcdN(*numeros):
    """Devuelve el máximo común divisor de varios números."""
    return reduce(math.gcd, numeros)

if __name__ == "__main__":
    import unittest

    class TestPrimos(unittest.TestCase):
        def test_esPrimo(self):
            self.assertEqual([n for n in range(2, 50) if esPrimo(n)], [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
        def test_primos(self):
            self.assertEqual(primos(50), (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47))
        def test_descompon(self):
            self.assertEqual(descompon(36 * 175 * 143), (2, 2, 3, 3, 5, 5, 7, 11, 13))
        def test_mcm(self):
            self.assertEqual(mcm(90, 14), 630)
        def test_mcd(self):
            self.assertEqual(mcd(924, 780), 12)
        def test_mcmN(self):
            self.assertEqual(mcmN(42, 60, 70, 63), 1260)
        def test_mcdN(self):
            self.assertEqual(mcdN(840, 630, 1050, 1470), 210)

    unittest.main(verbosity=2)
