#sexo = input("Digite o seu sexo:")
#if sexo == "masculino" or sexo == "feminino":
#   print("Sexo válido")
#
#else:
#    print("Sexo inválido")

salario = float(input("Digite o valor do seu salario:"))

if salario < 500:
    novo_salario = salario * 1.15
    print(f"O seu novo salario é {novo_salario} .")

else:
    if salario >= 1000:
        novo_salario = salario * 1.10
        print(f"O seu novo salario é {novo_salario} .")
    else:
        novo_salario = salario * 1.05
        print(f"Seu novo salario é: {novo_salario}")
