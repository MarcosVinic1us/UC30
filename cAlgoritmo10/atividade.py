paciente = {}

paciente["nome"] = input("Qual o seu nome:")
paciente["idade"] = int(input ("Quantos anos você tem"))
paciente["idade"] = int(input ("Digite seu peso (KG)"))
paciente["idade"] = int(input ("Digite sua altura(m)"))

imc = paciente ["peso"] / (paciente ["altura"]** 2)

paciente["imc"] = imc

print("\n Dados")
print("Nome:", paciente ["nome"])
print("Idade:", paciente ["idade"])
print("Idade:", paciente ["peso"])
print("Idade:", paciente ["altura"])
print("Idade:", round(paciente ["altura"]))