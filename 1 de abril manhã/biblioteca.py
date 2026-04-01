#SISTEMA DE GESTÃO DE BIBBLIOTECA

#DICIONÁRIO PARA ARMAZENAR OS LIVROS
catalogo = {}

#DICIONÁRIO PARA ARMAZENAR OS EMPRESTÍMOS
empretimoAtivo = {}

#lista para armazenar o histórico
historico = []

def adicionarlivro(codigo,titulo,autor,quantidade):
    if codigo in catalogo:
        print("Erro: livro com código {código}  já existe!")

    catalogo [codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }

    print(f"Livro '{titulo}'adicionado com sucesso")
    return True 

if codigo not in catalogo:
    print(f"Erro: Livro com código {codigo} não encontrado!")
    return False

if catalogo[codigo]["quantidade"] <= 0:
    print(f"Erro: ")





livros_do_aluno = conta_livros_aluno(nome_aluno)
if livros_do_aluno >= 2:
    print("Erro: {nome_aluno} já pegou 2 livros (limite máximo)")
    return False 