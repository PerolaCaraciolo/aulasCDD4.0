# Problema 02:

# Faça um código que receba as 3 notas de um aluno e verifique se ele está aprovado ou reprovado.
# Considere que a média para aprovação é 7,0.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3)/3

print(f"A média foi: {media}")
if media >= 7:
    print("== Aprovado ==")
else:
    print("== Reprovado ==")