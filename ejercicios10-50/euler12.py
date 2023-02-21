#Numero triangular 
import math

def numero_triangular(num):
	numerotriangular = (num * (num + 1)) / 2
	return int(numerotriangular)

def divisores(nu):
	divisores = 1
	for x in range(1,nu):
		if(nu % x == 0):
			divisores += 1
	return divisores

indice = 1
while True:
	if (divisores(numero_triangular(indice)) > 500):
		print(numero_triangular(indice))
		break
	indice += 1

"""
def numerotriangular_altamenteDivisible(divisores):
	for x in itertools.count(start=1):
		contadorDivisores = 0
		triangular = numero_triangular(x)
		for i in range(1,triangular + 1):
			if (triangular % i == 0):
				contadorDivisores += 1
		if (contadorDivisores > divisores):
			print(triangular)
			break
numerotriangular_altamenteDivisible(500)
"""





