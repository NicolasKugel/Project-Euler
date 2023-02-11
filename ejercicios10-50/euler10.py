"""
	la suma de los numeros primos por debajo de 10 = 17
	17 = 2 + 3 + 5 + 7

"""
import math

def no_primo(num):
	raizCuadrada = (int(math.sqrt(num)) + 1)
	for x in range(2,raizCuadrada):
		if((num % x) == 0):
			return False
	return True

	
def sumPrimesBellow(num):
	sum = 2
	for i in range(3,num):
		if (no_primo(i)):
			sum += i
	print(sum)

sumPrimesBellow(2000000)