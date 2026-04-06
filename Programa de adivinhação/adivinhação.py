roleta = [1,2,3,5,6,7,8,10,11,12,23,14,15,16,1718,19,20,21,22,23,24,25,26,27,28,29,30,31,32,34,35,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,67,68,69,70,71,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
import random
a = bool(True)

tentativas = 0
numeroRoletado = random.choice(roleta)

while True:
    numeroEscolhido = int(input("Digite qualquer valor entre um e cem"))
    if numeroEscolhido ==  numeroRoletado:
        print("Parabéns! Você acertou o número!")
        break
    elif numeroEscolhido < numeroRoletado:
        print("O número escolhido é maior do que o número roletado")
    else:
     print("O número escolhido é maior que o número roletado")

print(f"Você acertou o número em {tentativas} tentativas.")
