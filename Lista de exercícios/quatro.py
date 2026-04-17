# questão 4

float(input("Digite o seu peso em kg"))
float(input("Digite sua altura em metros"))

imc = peso / (altura ** 2)

print("Seu imc é: {imc:.2f}")

if imc < 24.9:
        print("Você se encontra magro")

else:
        print("Você não se encontra magro")

