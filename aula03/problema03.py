# Problema 03:

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3)/3

print("A média foi:", media)
if media >= 7:
    print("== Aprovado ==")
elif 7 > media > 4:
    print("== Aluno em recuperação ==")
else: print("== Reprovado ==")