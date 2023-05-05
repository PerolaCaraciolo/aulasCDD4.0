# Revisão 08:

# Faça um algoritmo que receba 4 números e realize a soma deles e a
# média entre eles. Imprima os resultados.

soma = 0

for x in range(4):
    num = float(input("Digite um número: "))
    soma += num

media = soma/4

print(f" Soma: {soma}\n Média: {media}")     # Só imprimi diferentinho pra ficar bonitinho apapagaiado memso, hihi.
