a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C:"))

if a < b + c or b < a + c or c < a + b :
    print("É possível formar um triângulo com esses lados")
    if  a == b == c:
        print("O triângulo é equilátero")
    elif a != b != c:
        print("O triângulo é escaleno")
    else:
        print("O triângulo é isósceles")
else:
    print("Não é possível formar um triângulo com esses lados")

