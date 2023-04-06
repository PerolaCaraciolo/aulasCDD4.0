# Problema 03:

# Escreva um algoritmo para ler 10 números e ao final da leitura, escrever a soma total dos 10 números lidos.

soma = int(0)

for x in range(10):
    num = int(input("Digite um número: "))
    soma += num     # É a mesma coisa que   " soma = soma + num "
#    print(soma)            Eu tenho o costume de colocar a impressão a cada laço de repetição só pra conferir
#                           que está sendo feito certinho. Depois tiro e deixo só a impressão que importa mesmo.

print(f"A soma de todos os números adicionados é {soma}.")
