

numeros = [91, 34, 67, 15, 82]
print("Lista original:", numeros)


numeros.sort()
print("Após sor():", numeros)


numeros.sort(reverse=True)
print("Após sort():", numeros)



print("Lista embaralhada", numeros)

import random

numeros = [6, 7, 8, 9, 10]
print("Lista original:", numeros)


numeros.sort()
print("Após sor():", numeros)


numeros.sort(reverse=True)
print("Após sor():", numeros)


random.shuffle(numeros)
print("Lista embaralhada", numeros)