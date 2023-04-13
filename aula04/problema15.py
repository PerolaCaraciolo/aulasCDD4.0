# Problema 15:

# Faça um código que receba o número de alunos de uma sala de aula e depois solicite as notas
# desses alunos, no final, mostre a média aritmética da turma.

alunos = int(input("Quantos alunos essa turma possui? "))
soma = 0
count = 0

while count < alunos:
    notas = float(input("Digite cada nota desses alunos, uma por vez: "))
    soma += notas
    count += 1

print(f"A média aritmética das notas dos alunos desta turma foi {soma/alunos}")
