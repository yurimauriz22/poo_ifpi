soma_das_notas = 0
quantidade = 0
while True:
    nota = float(input("Digite a sua nota quando quiser para digite -1: "))
    if nota == -1:
        break
    soma_das_notas += nota
    quantidade += 1

    if nota > 0:
        media = soma_das_notas / quantidade
        print(f"A media das notas é {media}")
    else:
        print("Nenhuma nota foi inserida.")