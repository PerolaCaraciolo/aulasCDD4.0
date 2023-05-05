# Revisão 20:

# Escreva um algoritmo que receba do usuário 10 números e mostre:
# 1. todos os números ímpares;
# 2. todos os números pares;
# 3. todos os números positivos;
# 4. todos os números negativos;
# 5. Quantos zeros aparecem no array.

num = []
par = []
impar = []
posit = []
negat = []
zeros = 0
posicaoZeros = []

for x in range(10):
    num.append(int(input("Digite um número: ")))

for x in range(10):
    if num[x] % 2 == 0:
        par.append(num[x])
    else:
        impar.append(num[x])
    if num[x] >= 0:
        posit.append(num[x])
    else:
        negat.append(num[x])
    if num[x] == 0:
        posicaoZeros.append(x)
        zeros += 1

print(f"Par: {par} \nÍmpar: {impar} \nPositivo: {posit} \nNegativo: {negat} \n{zeros} zero(s) na(s) posição(ões): {posicaoZeros}")
