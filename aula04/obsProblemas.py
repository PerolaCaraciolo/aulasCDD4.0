
# TRAGO NESTE ARQUIVO UM COMPILADO DOS MECANISMOS USADOS NOS PROBLEMAS DA AULA 04:


""" LAÇOS DE REPETIÇÃO: Quando usar 'FOR' e quando usar 'Whille'"""

# O "FOR" eu uso quando JÁ SEI A QUANTIDADE de vezes que preciso repetir aquele laço.
                # Eu crio uma variável no início do "FOR" e já dou como argumentos o início e fim de seus valores.
# O "WHILLE" eu NÃO SEI A QUANTIDADE de vezes, mas sei uma CONDIÇÃO que encerra aquele laço.
                #


""" Exemplo como no Problema 02 """
print("="*20, "02 :)")

#       range ( [start], stop, [step] )        Onde o que está entre [ ] não tem obrigatoriedade de estar argumentado,
#                                              apenas o STOP que tem.
# O STOP não é inclusivo, LOGO ele não participa do processo! Pois o START é sempre no índice "0", então vai ser até
# o último " - 1".
# O STEP mostra "de quanto em quanto" aquela contagem vai ser feita.

for contador in range(1, 10):   # Vai do "1" até o "9".
    print(contador)
print(".")
for contador in range(10):   # Vai do "0" até o "9".
    print(contador)
print(".")
for contador in range(1, 11):   # Vai do "1" até o "10"
    print(contador)
print(".")
for contador in range(1, 11, 2):   # Vai do "1" até o "10" a cada dois.
    print(contador)


""" Exemplo como no Problema 03 """
print("="*20, "03 :)")

n1 = 6
n2 = 2
print(f"({n1}+={n2}) = ({n1}={n1}+{n2}) >>> {n1+n2} ")
# Aqui foi só pra lembrar a forma de usar esse operador de atribuição " += ".


""" Exemplo como no Problema 04 """
print("="*20, "04 :)")

# Dá pra utilizar a contagem da própria variável que eu crio dentro do "FOR" como um "contador", que vai aumentando.
# Lembrando sempre que se eu quero usar também o último número, vou ter que adicionar "1" a ele.

num = 2     # Você pode mudar aqui pra testar! :D
for tabuada in range(1, 11):
    print(f"{num} * {tabuada} = {num*tabuada}")


""" Exemplo como no Problema 05"""
print("="*20, "05 :)")

# O "RANGE" pode receber como argumento tanto um número já quanto uma variável. E vale ter a atenção de analisar sempre
# que o STOP não é inclusivo. Pra ele participar da operação eu preciso somar uma unidade (+1)

for x in range(1, 11):
    print(x)
print(".")
exemplo = 10     # Você pode mudar aqui pra testar! :D
for x in range(1, exemplo+1):
    print(x)
