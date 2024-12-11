# 8. Calculadora de Potência Elétrica:
# • Receba a tensão e a corrente elétrica.
# • Calcule e exiba a potência elétrica.

tensao = float(input("Digite o valor da tensão em volts:"))
corrente = float(input("Digite o valor da corrente em amperes: "))
potencia = tensao * corrente
print(f"A potência elétrica é: {potencia} watts")
