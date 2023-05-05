# Revisão 21:

# Dado o seguinte array [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60] .
# Crie um novo array com os dados que estão entre os índices 3 e 8.

origin = [10, 12, 20, 30, 25, 40, 32, 31, 35, 50, 60]
novo = []

for x in range(4, 8):
    novo.append(origin[x])
print(novo)
