# Problema 03:

# (02) - Faça um código que receba as 3 notas de um aluno e verifique se ele está aprovado ou reprovado.
# (02) - Considere que a média para aprovação é 7,0.

# Utilize o código do problema 02 e acrescente a opção de "aluno em recuperação", caso sua média
# seja menor que 7,0 e maior que 4,00.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3)/3

print("A média foi:", media)
if media >= 7:
    print("== Aprovado ==")
elif media >= 4:           # O "ELIF" aparece sempre que tenho mais que duas alternativas pra usar dentro de um "IF".
                           # Entre o "IF" e o "ELSE".
    print("== Aluno em recuperação ==")
else:
    print("== Reprovado ==")


# Eu tinha colocado "7 > media >= 4" no "ELIF", mas realmente não precisa pq já tenho uma parte dessas informações no
# "IF" de cima.
