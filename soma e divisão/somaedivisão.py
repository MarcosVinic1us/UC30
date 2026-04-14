a = int(input("Digite um valor"))
b = int(input("Digite outro valor"))

def soma_segura (a,b):
    resultado = a + b
    return resultado
try:
    soma_segura
except: TypeError:
    print("Erro: Os valores deves ser números")