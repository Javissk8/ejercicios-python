"""
lista = [1,2,3,4,5,6,7]

for i in range(len(lista)):
	suma = lista[i] + lista[i]
	lista[i] = suma
print(i)
"""
'''
lista = [1,2,3,4,5,6,7]
i = 0
while i < len(lista):
	lista[i] = lista[i] + lista[i]
	i += 1
print(lista)
'''
'''
lista = [1,2,3,4,5,6,7,3]
i = 0

while i < len(lista):
	if(lista[i]==3):
		print("encontre el 3, en la posicion {}".format(i))
		
	else:
		print("continuo buscando")
		i += 1
'''
'''
-----
i = 0
j = 0
while i < 100:
	print(i)
	i += 1
	j = j + i
	print(j)
print(j)
----
'''
'''
i = 0
j = 0
for i in range (0,100):
	print(i)
	i += 1
	j = j + i
	print(j)
print(j)
'''
'''
impares = 0
for i in range(1,101):
	if i%2!=0:
		impares += 1 
		print(i)
print(impares)
'''
'''
impares = 0
i = 0
while i < 100:
	i += 1
	if i % 2 != 0:
		impares += 1
		print(i)
print(impares)
'''
'''
i = 1
print("escribe el numero al que quieres llegar")
j = int(input())
while i <= j:
	print(i)
	i += 1
'''
'''
lista = []
print("introduce un string")
palabra = ""
while palabra != "exit":
	palabra = input()
	lista.append(palabra)

print(lista)
print(len(lista))
'''
'''
print("dime si si o no ")
decision = input()
while decision != "si":
	if decision == "no":
		print("seguro?")
		decision = input()
	else:
		print("esa opcion no es valida")
		break
'''
'''
i = 1
print("escribe un numero")
j = int(input())
k = 0
while i <= j:
	if i % 3 == 0:
		print(i)
		k += 1
	i += 1
print(k)
''' 
'''
i = 0
pares = 0
impares = 0
while i <+ 100:
	i += 1
	if i % 2 != 0:
		impares += 1
		print(i)
	else:
		pares += 1 
		print(i)
print(impares)
print(pares)
'''
i = 1
print("escribe un numero")
j = 0
k = 0
while i <= 100:
	if i % 3 == 0:
		print(i)
		k += 1 
	if i % 2 == 0:
		print(i)
		j += 1
	i += 1
print(k)
print(j)
