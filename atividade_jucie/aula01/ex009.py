# 9. Calculadora de Volume de um Cilindro:
# • Receba o raio e a altura de um cilindro.
# • Calcule e exiba o volume do cilindro.
import math
pi = math.pi
raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))
volume = pi * (raio ** 2) * altura
print(f"O volume do cilindro é {volume} m³")