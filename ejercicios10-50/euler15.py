"""
2**15 = 32768
la suma de sus digitos es igual a 26

2** 1000 ¿Cual es la suma de sus digitos?
"""

def sumaDigitosDePotencia(x, y):
    potenciacion = x ** y
    resultado = 0
    for x in str(potenciacion):
        resultado += int(x)
    print(resultado)

sumaDigitosDePotencia(2, 1000)