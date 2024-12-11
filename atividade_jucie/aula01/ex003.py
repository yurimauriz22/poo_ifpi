# 3. Calculadora de IMC:
# • Receba o peso e a altura de uma pessoa.
# • Calcule e exiba o Índice de Massa Corporal (IMC).

altura = float(input("Digite a sua altura:"))
peso = float(input("Digite o seu peso:"))
imc = peso / (altura ** 2)
print(f"Seu IMC é {imc}")