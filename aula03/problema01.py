# Problema 01:

# Receba 2 números do usuário e mostre eles em ordem crescente.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite mais um número: "))    # Se eu não definir como número, não vai ser possível fazer as
                                              # compações de > ou < !

if n1 != n2:    # Eu primeiro analiso se os números são diferentes ou não, porque eu posso economizar a quantidade de
                 # processamentos feitos.
                 # "ELES SÃO DIFERENTES? << sim >> então TEMOS OUTRA PERGUNTA: um número OU É MAIOR OU É MENOR que o outro"
                 # "ELES SÃO IGUAIS? << sim >> então NÃO TEM O QUE ANALISAR."
    if n1 < n2:           # "IF" aninhado: um dentro do outro.
        print(f"Em ordem crescente, os números foram: {n1} e {n2}.")
    else:    # Se só tenho duas possibilidades de condições, no momento em que deixo a primeira clara no "IF", o "ELSE"
             # dispensa qualquer coisa escrita, porque ele já entende.
        print(f"Em ordem crescente, os números foram : {n2} e {n1}")
else:
    print("ERRO! Os números são iguais.")

#   OOOOOOUUUUUU:
                    # Essa forma é como a anterior, só inverte onde está o diferente e o igual !!!
"""
if n1 == n2 :
    print("ERRO! Números iguais.")
else:
    if n1 < n2 :
        print(f"Em ordem crescente, os números foram: {n1} e {n2}.")
    else:
        print(f"Em ordem crescente, os números foram: {n2} e {n1}.")
"""


# Eu tinha feito como abaixo antes, mas acaba processando mais coisas no caso de eles serem iguais, porque teria
# que fazer até 3 conferências:   " é maior? / é menor? / É IGUAL! "
# E da forma de lá de cima, ele só faria no máximo 2 conferências:   " é diferente? / É IGUAL! "

"""if n1<n2:
    print(f"Em ordem crescente, os números foram: {n1} e {n2}.")
elif n1>n2:
    print(f"Em ordem crescente, os números foram {n2} e {n1}.")
else:
    print("ERRO! Números iguais.")"""
