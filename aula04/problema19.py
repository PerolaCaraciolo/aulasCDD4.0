# Problema 19:

# Escreva um código que solicite o nome completo do usuário e mostre
# quantas letras tem esse nome.

nome = input("Digite seu nome completo: ")
count = 0

for x in nome:
    if x != " ":
        count += 1
        print(count)
