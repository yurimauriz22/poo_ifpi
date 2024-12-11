def cadastar_clientes():
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    telefone = input("Digite seu telefone: ")
    return f"nome: {nome} , email: {email}, telefone: {telefone}"

def cadastar_livros():
    titulo = input("Digite o titulo do livros: ")
    autor = input("Digite o autor do livro: ")
    ano_de_publicacao = input("Digite o ano de publicação: ")
    return f"titulo: {titulo} , autor: {autor}, ano de publicação: {ano_de_publicacao}"

def listar_clientes(clientes):
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    print("=== Lista de Clientes ===")
    for cliente in clientes:
        print(cliente)

def listar_livros(livros):
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    print("=== Lista de Livros ===")
    for livro in livros:
        print(livro)