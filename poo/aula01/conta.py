#Variavel
def criar_conta(nome, numero, saldo, limite):
    conta = {'nome': nome, 'numero': numero, 'saldo': saldo, 'limite': limite}
    return conta

#Funcionalidades
def depositar(conta, valor):
    conta['saldo'] += valor

def sacar(conta, valor):
    conta['saldo'] -= valor

def extrato(conta):
    print(f'Nome: {conta['nome']} --> Saldo: {conta['saldo']}.')
    

conta1 = criar_conta('Yuri', 1234, 24.44, 10000)
# print(conta1)
conta2 = criar_conta('PP', 4321, 255.55, 20000)
# print(conta2)

depositar(conta1, 100)
print(conta1)
depositar(conta2, 200)
print(conta2)

extrato(conta1)
extrato(conta2)