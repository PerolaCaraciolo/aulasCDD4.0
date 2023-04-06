# Problema 05:

# Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma:
# E - Etanol, G - Gasolina), calcule e imprima o valor a ser pago pelo cliente, sabendo-se que o preço do litro da
# gasolina é R$ 5,80 e o preço do litro do etanol é R$ 4,90

combustivel = input("Qual tipo de combustível você adquiriu? \nDigite 'E' para Etanol ou 'G' para gasolina. \n")

if combustivel in "Gg" or combustivel in "Ee":     # Dessa forma eu consigo aceitar tanto Maiúsculo quanto Minúsculo!
    litros = float(input(f"Quantos litros de {combustivel} você adiquiriu? "))
    if combustivel in "Gg":
        precoG = litros*5.8
        print(f"O valor a ser pago pelo cliente é de R${precoG}.")
    else:
        precoE = litros*4.9
        print(f"O valor a ser pago pelo cliente é de R${precoE}.")
else:               # Se ele não ne responder o que me interessa, eu já nem vou perguntar mais nada.
    print("Informação inválida!")


#   OOOOOOUUUUUU:
                    # Essa forma abaixo também é correta, só que ele só vai aceitar "G" e "E" maiúsculos !!!
"""
if combustivel != "G" or combustivel != "E":
    print("Informação inválida!")
else:
    litros = float(input(f"Quantos litros de {combustivel} você adiquiriu? "))
    if combustivel == "E":
        precoE = litros*4.9
        print(f"O valor a ser pago pelo cliente é de R${precoE}.")
    else:
        precoG = litros*5.8
        print(f"O valor a ser pago pelo cliente é de R${precoG}.")
"""
