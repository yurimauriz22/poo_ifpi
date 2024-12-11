num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operação = int(input("Escolha a operação: "))
if operação == 1:
    resultado = num1 + num2
    print(f"o resultado da soma é {resultado}")
elif operação == 2:
    resultado = num1 - num2
    print(f"o resultado da subtração é {resultado}")
elif operação == 3:
    resultado = num1 * num2
    print(f"o resultado da multiplicação é {resultado}")
elif operação == 4:
    resultado = num1 / num2
    print(f"o resultado da divisão é {resultado}")
else:
    print("operação invalida")