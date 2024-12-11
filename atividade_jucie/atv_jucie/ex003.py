nota = float(input("Digite sua nota:"))
if nota >= 7:
    print("Aprovado")
elif 5 <= nota and nota < 7:
    print("Recuperação")
else:
    print("Reprovado")