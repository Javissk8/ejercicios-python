import random
veces = [0]
numero = random.randint(1,100)
print(numero)
num = 1
actual = 0
prev = 0
i = 0
while num >= 1 and num <= 100 and i < 1:	
	
	print("adivina el numero")
	num = int(input())
	if num != numero:
		veces.append(num)
		actual = numero - num
		if abs(actual) <= 10:
			print("warm!")
		elif abs(actual) > 10:
			print("cold!")
		i =+ 1 
	else: 
		print("correcto")
		print("lo intentaste: ", len(veces), "veces")
		break	
while num >= 1 and num <= 100:	
	print("adivina el numero")
	num = int(input())
	if num != numero:
		veces.append(num)
		prev = actual
		actual = abs(numero - num)
		if actual < prev:
			print("warmer!")
		elif actual > prev:
			print("colder!") 
	else: 
		print("correcto")
		print("lo intentaste: ", len(veces), "veces")
		break	
	
