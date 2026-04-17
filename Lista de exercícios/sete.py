# questão 7

vendas = [
    {"numero": 101, "valor": 50},
    {"numero": 202, "valor": 75},
    {"numero": 303, "valor": 20},
    {"numero": 404, "valor": 100}
]

soma_pares = sum(v["valor"] for v in vendas if v["numero"] % 2 == 0)

print(soma_pares)