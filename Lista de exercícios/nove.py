notas = [5.5, 7.0, 8.2, 6.8, 9.0, 7.5]

contador = 0

for nota in notas:
    if nota > 7:
        contador += 1

print("Quantidade de notas acima de 7:", contador)