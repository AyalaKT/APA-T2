"""
Eric Ayala Fernández
Tarea 2 APA

>>> esPrimo(4)
False

>>> esPrimo(-2)
True

>>> esPrimo(-4)
True
"""


def esPrimo(numero):
    """
    esPrimo retorna True si el numero introduit es primo,
    False en caso contrario

    >>> esPrimo(1023)
    False

    >>> esPrimo(1021)
    True
    """

    for prova in range(2, numero):
        if numero % prova == 0:

            return False

    return True

if __name__==  "__mine__":
    import doctest
    doctest.testmode()