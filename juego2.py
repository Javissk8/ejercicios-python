import random
numRandom = random.randint(1,100)
intentos = []
numIn = 0
prev = 0
actual = 0
win = False
while win == False:
	print(numRandom)
	numIn = int(input("adivina el numero"))
	intentos.append(numIn)
	if numIn == numRandom:
		print("ya ganaste!")
		win = True
		print("lo intentaste :", len(intentos), "veces")
	else:
		if numIn < 1 or numIn > 100:
			print("out of bounds")
			continue
		if len(intentos) == 1:
			actual = abs(numIn - numRandom)
			if actual <= 10:
				print("warm!")
			else:
				print("cold!")
		else:
			prev = actual
			actual = abs(numIn - numRandom)
			if prev > actual:
				print("warmer")
			elif prev < actual:
				print("colder")
			else:
				print("el numero es el mismo")

	