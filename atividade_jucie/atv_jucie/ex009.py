altura = float(input("Digite a sua altura:"))
peso = float(input("Digite o seu peso:"))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("Abaixo do peso")
elif 18.5 <= imc < 24.9:
    print("Peso normal")
elif 24.9 <= imc < 29.9:
    print("Sobrepeso")
elif imc >= 30:
    print("Obesidade")
