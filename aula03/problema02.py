# Problema 02:

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3)/3

print(f"A média foi: {media}")
if media >= 7:
    print("== Aprovado ==")
else: print("== Reprovado ==")
