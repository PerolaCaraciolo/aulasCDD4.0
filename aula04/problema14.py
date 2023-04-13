# Problema 14:

# Ler 10 valores, calcular e escrever a média aritmética desses valores lidos (usando While).

x = 10
soma = 0
count = 0

while count < x:
    valores = int(input("Digite um valor: "))
    soma += valores
    count += 1

print(f"A média dos valores informados é {soma/x}.")
