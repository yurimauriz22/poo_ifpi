from func import *
clintes = []
livros = []

while True:
    print("=== Menu Principal ===")
    print("1. Cadastrar cliente")
    print("2. Cadastrar livro")
    print("3. Listar clientes")
    print("4. Listar livros")
    print("5. Sair")
    
    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        cliente = cadastar_clientes()
        clintes.append(cliente)
        print("Cliente cadastrado!!")
    elif escolha == "2":
        livro = cadastar_livros()
        livros.append(livro)
        print("Livro cadastrado!!")
    elif escolha == "3":
        listar_clientes(clintes)
    elif escolha == "4":
        listar_livros(livros)
    elif escolha == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida tente denovo!!")
    