# Revisão 01:

# 1. Faça um algoritmo que receba 2 notas e calcule a média aritmética.
# 2. Imprimir se aprovado, em recuperação ou reprovado.
# 3. Perguntar se quer repetir.
# 4. Salvar as médias em um array e imprimir.

sim = 1
medias = []

while sim == 1:
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))

    media = (n1+n2)/2
    medias.append(media)

    print(f"Média: {media}")

    if media >= 7:
        print("APROVADO!")
    elif media >= 4:
        print("RECUPERAÇÃO!")
    else:
        print("REPROVADO!")

    sim = int(input("\n1 - Deseja repetir \n2 - Encerrar \n"))
    if sim == 1:
        continue
    else:
        print(f"Médias de todos os alunos: {medias}")