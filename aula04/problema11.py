# Problema 11:

# Ler 10 valores e escrever quantos desses valores lidos são NEGATIVOS.

negativos = 0

for num in range(10):
    valor = int(input("Digite um número inteiro (positivo ou negativo): "))
    if valor < 0:
        negativos += 1

print(f"Você digitou {negativos} número(s) negativo(s).")
