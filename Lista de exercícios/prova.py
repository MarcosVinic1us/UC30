# questão 3

tal = 0.0

while True:
    
    valor = float(input("Digite o valor do item (ou 0 para finalizar): "))
    
    
    if valor == 0:
        break
    
    
    total += valor


print(f"Total da compra: R$ {total:.2f}")