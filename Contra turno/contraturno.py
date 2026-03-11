aluno = []
aluno["nome"] = input("Digite o nome do aluno:")
aluno["nota1"] = float("Digite a nota 1:")
aluno["nota2"] = float("Digite a nota 2:")

media = (aluno ["nota1"] + aluno["nota2"])
aluno["media"] = media

if media >= 7:
    situacao = "Aprovado"
elif  media >= 5:
    situacao = "Recuperação"
else:
    situacao= "Reprovado"
    
    print("\n Dados do aluno:")
    for chave, valor in aluno.items():
     print(f"{chave }: valor")

     print("Situação:", situacao)