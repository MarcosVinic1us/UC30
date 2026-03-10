matricula1 = 202601
nome1 = "Ana Silva"
telefone1 = "9999-8888"

aluno = {
    "matricula": 202601,
    "nome": "Ana Silva",
    "telefone": "9999-8888"
    }
print(aluno)

contato = {
"@camilaqueiroz" : "Camila Queiroz",
"@brunamarquezine" : "Bruna M.",
"@sheronmenezes": "Sheron M.",
"@Joao ": "Joao O."
}
print(contato)
print(type(contato))

print(contato ["@camialqueiroz"])

print(contato.get ["@paolaoliveira"])
print(contato.get ["@inesistente"])
print(contato.get ["@inesistente", "Nao encontrado"])

contato["@giovanna"] ="Giovanna"
print("Após add", contato)

contato["@paolaoliveira"] = "Paola Oliveira",
print("Após add", contato)

contato.update ({
    "@brunamarquezine": "Bruna Marquezine",
    "@camilaqueiroz" : "Camila Q"
})
print("Após atualização", contato)

removido = contato.pop("@paolaoliveira")
print("Removida: {removido}")
print("Após o pop: ", contato)

copia = dict(contato)
contato.clear()
print("Após o clear:", contato)
print("copia:", copia)

print("Número de contatos", len(contato))

if "@Joao"in contato:
    print(f"Encontrado: {contato ['@joao']}")
    if "@joao" in contato:
        if "@inexistente" in contato:
            print("existe")
else: 
    print("nao existe.")