#1. Calculadora de Descontos:
#•Receba o preço original de um produto e a porcentagem de desconto.
#•Calcule e exiba o preço final após o desconto.
preco_inicial = float(input("Digite o preço original do produto:"))
porcentagem = float(input("Digite o valor da porcentagem:"))

desconto = (porcentagem / 100) * preco_inicial
preco_final = preco_inicial - desconto
print(f"Com o desconto o valor final vai ficar {preco_final}")