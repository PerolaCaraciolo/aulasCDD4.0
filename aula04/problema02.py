# Problema 02:

# Faça um programa que mostre na tela, a contagem de 1 ate 10.

for x in range(1, 11):      # ESTRUTURA DO "RANGE" >>> range([start], stop[, step])
    print(x)                # O que está entre [ ] é porque não é obrigatório de ter argumentado. Apenas o STOP que é!
                            # E lembrando que o START automático é do "0" e o STOP vai até um número antes do que é
                            # argumentado no "FOR", porque o índice de posição dos caracteres começa em "0".

print(".")
# Imprima a contagem de 1 até 10 mas a cada dois números.

for x in range(1, 10, 2):     # O "Step" delimita de quanto em quanto ele vai contar.
    print(x)
