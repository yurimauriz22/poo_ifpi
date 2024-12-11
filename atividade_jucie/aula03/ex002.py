numero_secreto = 30

while True:
    numero_usuario = int(input('Digite um número entre 1 e 100: '))
    if numero_usuario == numero_secreto:
        print(f'Parabéns, você acertou o número secreto! que era {numero_secreto}')
        break
    elif numero_usuario < numero_secreto:
        print('Tente um número maior!')
    elif numero_usuario > numero_secreto:
        print('Tente um número menor!')
