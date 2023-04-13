# Problema 18:

# Refaça o exercicio anterior, agora implementando a pergunta:
# “Deseja realizar novo cálculo?”

# Escreva um código para ler as notas da 1a. e 2a. avaliações de um aluno. Calcule e imprima a média desse
# aluno. Só devem ser aceitos valores válidos durante a leitura (0 a 10) para cada nota.

nota1 = float(input("Digite a primeira nota: "))
while nota1 > 10 or nota1 < 0:
    nota1 = float(input("NOTA INVÁLIDA! \nDigite novamente: "))
nota2 = float(input("Digite a segunda nota: "))
while nota2 > 10 or nota2 < 0:
    nota2 = float(input("NOTA INVÁLIDA! \nDigite novamente: "))

print(f"A média do aluno referido foi {(nota1+nota2)/2}. \n")

continuar = input("Deseja realizar cálculo da média de outro aluno? S ou N: ")

if continuar in "Ss":
    nota1 = float(input("Digite a primeira nota: "))
    while nota1 > 10 or nota1 < 0:
        nota1 = float(input("NOTA INVÁLIDA! \nDigite novamente: "))
    nota2 = float(input("Digite a segunda nota: "))
    while nota2 > 10 or nota2 < 0:
        nota2 = float(input("NOTA INVÁLIDA! \nDigite novamente: "))

    print(f"A média do aluno referido foi {(nota1+nota2)/2}.")


# Se eu coloco while, teria que ser um dentro do outro pra poder continuar tbm perguntando se quer continuar ou não.
# COMO SERIA A MELHOR FORMA NESSE CASO?          ?????????????? PERGUNTAR NA AULA!
# Acabei usando "IF" mesmo pra ser uma vez só.
