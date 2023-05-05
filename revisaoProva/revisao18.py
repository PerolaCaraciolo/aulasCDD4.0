# Revisão 18:

# Escreva um algoritmo que, dado um arrays, retorne um novo array com os elementos em ordem invertida.
# Entrada:  a=[2,5,4,2,8,5,2]
# Saída:  b=[2,5,8,2,4,5,2]

certo = [2, 5, 4, 2, 8, 5, 2]
inverso = []

for x in range(6, -1, -1):
    inverso.append(certo[x])

print("Array inverso:", inverso)
