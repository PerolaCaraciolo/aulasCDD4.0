# Problema 16:

# Faça um código para ler 2 valores e realize a divisão do primeiro pelo
# segundo valor recebido. Caso o segundo valor digitado seja "0", solicite
# novamente o valor, informando que só aceitaremos valores diferentes de
# zero.


# EU TINHA INICIADO A IDEIA ASSIM:
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite mais um valor e, agora, diferente de '0': "))
while n2 == 0:
    n2 = int(input("VALOR INVÁLIDO! \nDigite novamente: "))

print(f"{n1}/{n2} = {n1/n2}")



# MOZI ME INDICOU DE ORGANIZAR O ÍNICIO ASSIM, e de fato ficou mais limpo. Preferi, só que não teria como
# imprimir uma mensagem diferente da primeira, pra indicar que tá inválido, então deixei da minha forma mesmo.
# (Eu tava na ideia como se os dois não pudessem ser zero KKcry)
"""
n1 = 0
n2 = 0
while n1 == 0:
    n1 = int(input("Digite novamente: "))
while n2 == 0:
    n2 = int(input("Digite novamente: "))
"""
