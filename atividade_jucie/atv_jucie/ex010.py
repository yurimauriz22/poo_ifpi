palavra = input("Digite a palavra: ")
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")