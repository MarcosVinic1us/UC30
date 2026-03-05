nomes = ["Ana","Bruno","Carlos", "Diana"]
print("Nomes:",nomes)

nomes.remove("Bruno")
print("LIsta atualizada:",nomes)


removido = nomes.pop(1)
print("Removido: {removido}")
print("Após pop():", nomes)


del nomes[0]
print("Após del nome [0]",nomes)


nomes.clear()
print("Lista atualizada:", nomes)