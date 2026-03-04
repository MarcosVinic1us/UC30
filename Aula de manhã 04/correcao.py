numero1 = float(input("Digite o 1ª número:"))
numero2 = float(input("Digite o 2 ª número:"))

soma = numero1 + numero2
produto = numero1 * numero2

print("Soma:", soma)
print("Produto", produto)

usuario = input("Digite seu user:")
senha = input ("Digite sua senha")

if (usuario == "procopio" and senha == "12345"):
    (usuario == "paiva" and senha == "54321")
print("Seja bem-vindo!")


print("Usuário e senha não conferem.")

nome = input("Digite seu nome:")
senhaCorreta = "123456"

tentativa = 3

while tentativa > 0:
    senha = input("Digite sua senha:")

    if senha == senhaCorreta:
        print(f"Olá, {nome}! Seja bem-vindo!")
        break
    else:
        tentativa -= 1
        print("Senha errada! Você tem 2 tentativas")

        if tentativa == 2:
            print("Senha errada! Você tem 2 tentativas")
        elif tentativa == 1:
            print("Senha errada! Você tem 1 tentativa.")
        else:
            print("Senha bloqueada!")