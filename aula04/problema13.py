# Problema 13:

# Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.

soma = 0

for qtd in range(10):
    valores = int(input("Digite um valor: "))
    soma += valores

print(f"A média dos números informados é {soma/10}.")
