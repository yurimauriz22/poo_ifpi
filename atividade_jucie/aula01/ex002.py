# 2. Conversor de Temperatura:
# • Receba uma temperatura em graus Celsius.
# • Converta e exiba a temperatura em Fahrenheit e Kelvin.

graus_celsius = float(input("Digite a sua temperatura em Celsius:"))
fahrenheit = graus_celsius * 1.8 + 32
kelvin = graus_celsius + 273
print(f"A sua temperatura em Fahrenheit é {fahrenheit} e sua temperatura em Kelvin é {kelvin}.")

