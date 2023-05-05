# Revisão 19:

# Usando While escreva um algoritmo que preencha um array A com os 10 primeiros números ímpares, iniciando por zero.
# Saída: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

inicial = []
count = 0

while count < 20:
    if count % 2 != 0:
        inicial.append(count)
    count += 1     # Eu tinha colocado o count tabulado dentro do "IF" e ele simplesmente não tava nem entrando no "WHILE"
                                    # POR QUEEEEEEÊ?      ???????????
print(inicial)
