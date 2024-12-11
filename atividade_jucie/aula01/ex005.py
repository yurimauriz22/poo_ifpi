# 5. Conversor de Moeda:
# • Receba um valor em reais e a taxa de câmbio.
# • Converta e exiba o valor em dólares.

reais = float(input("Digite o valor em reais:"))
taxa_cambio = float(input("Digite a taxa de cambio:"))
dolar = reais * taxa_cambio
print(f"O valor em dólares é: {dolar}") 