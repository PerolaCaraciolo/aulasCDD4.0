# Problema 05:

# Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma:
# E - Etanol, G - Gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da
# gasolina é R$ 5,80 e o preço do litro do etanol é R$ 4,90

combustivel = input("Qual tipo de combustível você adquiriu? \nDigite 'E' para Etanol ou 'G' para gasolina. \n")

if combustivel != "G" or combustivel != "E":   # combustivel in "Gg" or combustivel in "Ee" FAZER ESSE TESTE DPS
    print("Informação inválida!")
else:
    litros = float(input(f"Quantos litros de {combustivel} você adiquiriu? "))
    if combustivel == "E":   # combustivel in "Gg" vai considerar já o "G" e o "g"
        precoE = litros*4.9
        print(f"O valor a ser pago pelo cliente é de R${precoE}.")
    elif combustivel == "G":   # combustivel in "Ee"
        precoG = litros*5.8
        print(f"O valor a ser pago pelo cliente é de R${precoG}.")
    else:
        print("Informações inválidas!")