# Problema 03:

# Altere o código anterior e acrescente a opção de aluno em recuperação, caso sua média
# seja menor que 7,0 e maior que 4,00.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3)/3

print("A média foi:", media)
if media >= 7:
    print("== Aprovado ==")
elif media >= 4:   # Eu tinha colocado "7 >", mas realmente precisa não pq já tenho informação sobre o 7.
    print("== Aluno em recuperação ==")
else:
    print("== Reprovado ==")