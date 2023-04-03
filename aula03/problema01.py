# Problema 01:

# Receba 2 números do usuário e mostre eles em ordem crescente

n1 = int(input("Digite um número: "))
n2 = int(input("Digite mais um número: "))

if n1 != n2 :
    if n1 < n2 :
        print(f"Em ordem crescente, os números foram: {n1} e {n2}.")
    else:
        print(f"Em ordem crescente, os números foram : {n2} e {n1}")
else:
    print("ERRO! Os números são iguais.")

#   OOOOOOUUUUUU:
"""
if n1 == n2 :
    print("ERRO! Números iguais.")
else:
    if n1 < n2 :
        print(f"Em ordem crescente, os números foram: {n1} e {n2}.")
    else:
        print(f"Em ordem crescente, os números foram: {n2} e {n1}.")
"""


# Eu tinha feito assim, mas acaba processando mais coisas no caso de eles serem iguais.
# Da forma dele já faz, no máximo, duas análises.
"""if n1<n2:
    print(f"Em ordem crescente, os números foram: {n1} e {n2}.")
elif n1>n2:
    print(f"Em ordem crescente, os números foram {n2} e {n1}.")
else:
    print("ERRO! Números iguais.")"""