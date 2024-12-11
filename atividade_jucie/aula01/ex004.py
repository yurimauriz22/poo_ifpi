# 4. Cálculo de Juros Simples:
# • Receba o capital inicial, a taxa de juros e o tempo.
# • Calcule e exiba o montante final após os juros simples.

capital_inicial = float(input("Digite seu capital inicial:"))
taxa_juros = float(input("Digite a taxa de juros:"))
tempo = float(input("Digite o tempo:"))

juros_simples = capital_inicial * (taxa_juros / 100) * tempo
montante_final = capital_inicial + juros_simples
print(f"Apos o calculo o seu juros simples é {juros_simples} e somando com o valor inical fica {montante_final}" )