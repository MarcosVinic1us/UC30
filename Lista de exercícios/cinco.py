# questão 5

grupo1 = int(input("Digite o número dos seus amigos"))

grupo2 = int(input("Digite o restante"))

total_amigos = grupo1 + grupo2
print(f"Total de amigos: {total_amigos}")

if total_amigos % 2 == 0:
    print("A quantidade é par")

else:
    print("A quantidade é ímpar")