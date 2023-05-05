# Revisão 09:

# Faça um algoritmo que receba um número inteiro e mostre o seu antecessor.

num = int(input("Digite um número: "))

if num >= 0:
    print(f"O antecessor de {num} é {num-1}.")
else:
    print(f"O antecessor de {num} é {num+1}.")

# O professor resolveu assim considerando que o antecessor de número negativo tem regra diferente dos positivos, mas
# sincerameeeente... eu acho que segue o mesmo raciocício de que pra esquerda é antecessor e direita sucessor.
# Ex.: -5  tem -6 como ANTEcessor e -4 como SUCEssor.
# Eu entendo que o -4 é apenas maior que o -5, mas não entendo como antecessor não. :S
# Maaaaas como ele fez a questão assim, só deixei salva mesmo como ele fez até mostrar pra ele, mas a seguinte fiz certinha.
