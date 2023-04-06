# Problema 04:

# Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome do vencedor.
# Caso não haja vencendor, deverá ser impressa a palavra EMPATE.

time1 = input("Digite o nome do primeiro time: ")
time2 = input("Digite o nome do segundo time: ")
gols1 = int(input(f"Quantos gols o {time1} fez? "))
gols2 = int(input(f"Quantos gols o {time2} fez? "))

if gols1 != gols2:     # Mesma análise do Problema 01.
    if gols1 > gols2:
        print(f"O vencedor do jogo em questão foi o time {time1}.")
    else:
        print(f"O vencedor do jogo em questão foi o time {time2}.")
else:
    print("O jogo teve um EMPATE!")
