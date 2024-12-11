soma = 0
while True:
    num = int(input('Digite um número inteiro (0 para sair): '))
    if num == 0:
        break
    soma += num
    print(f'A soma total é {soma}')