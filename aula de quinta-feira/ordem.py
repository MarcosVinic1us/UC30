import random

numeros = [45, 12,78,23,56]
print("Lista original:", numeros)


numeros.sort()
print("Após sor():", numeros)


numeros.sort(reverse=True)
print("Após sor():", numeros)


random.shuffle(numeros)
print("Lista embaralhada", numeros)