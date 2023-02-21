"""
n → n/2 (n es par)

n → 3n + 1 (n es impar)

"""
secuenciaMasLarga = []
secuenciaCheck = []

indice = 3
while ( indice < 1000000):
	secuenciaCheck.append(indice)
	primero = indice
	while (primero > 0):
		if (primero == 1):
			break
		elif (primero % 2 == 0): #Si es par
			primero = int(primero / 2)
		else:
			primero = int(3 * primero + 1) #Si es impar
		secuenciaCheck.append(primero)
	if (len(secuenciaCheck) > len(secuenciaMasLarga)):
		secuenciaMasLarga = secuenciaCheck
	indice += 1
	secuenciaCheck = []

print(secuenciaMasLarga)









