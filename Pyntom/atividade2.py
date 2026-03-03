numero = int(input("Insira um número:"))

quadrado = numero * numero
cubo = numero * numero * numero
if(numero %2==0):
    print("Onúmero é par e ele ao quadrado é:", quadrado)
else:
    print("O número é ímpar e o seu cubo é:", cubo)