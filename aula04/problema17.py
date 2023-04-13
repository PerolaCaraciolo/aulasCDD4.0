# Problema 17:

# Escreva um código para ler as notas da 1a. e 2a. avaliações de um aluno. Calcule e imprima a média desse
# aluno. Só devem ser aceitos valores válidos durante a leitura (0 a 10) para cada nota.

nota1 = float(input("Digite a primeira nota do aluno: "))
while nota1 > 10 or nota1 < 0:     # Eu tinha colocado "10 < nota1 < 0" e ele não tava entrando mesmo assim, aí me
                                   # liguei que seria como se fosse "AND", o que não é o caso da questão!
    nota1 = float(input("NOTA INVÁLIDA! \nDigite novamente: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
while nota2 > 10 or nota2 < 0:
    nota2 = float(input("NOTA INVÁLIDA! \nDigite novamente: "))

print(f"A média do aluno referido foi {(nota1+nota2)/2}.")
