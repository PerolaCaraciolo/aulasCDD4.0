
# TRAGO NESTE ARQUIVO UM COMPILADO DOS MECANISMOS USADOS NOS PROBLEMAS DA AULA 03:


""" Exemplo como no Problema 01.1 """

# QUANTO MENOS PROCESSAMENTO eu faço, melhor meu código. E isso é MAIS IMPORTANTE que a quantidade de linhas que tenho.
# Se tenho dois números e quero o maior, a primeira grande pergunta pra saber isso é:
#        " ELES SÃO IGUAIS? << sim >>  então cabou-se, não tem como analisar um maior que outro.
#                           << não >>  então temos mais duas perguntas >>>>>>>       (O que gera um "IF" aninhado)
#        " N1 É MAIOR QUE N2? << sim >>  então N1 > N2
#                             << não >>  então N1 < N2


""" Exemplo como no Problema 01.2 """
print("="*20, "01.2 :)")

num1 = int(5)     # Você pode mudar aqui pra testar! :D
num2 = int(8)     # Você pode mudar aqui pra testar! :D
if num1 != num2:
    # Ter um "IF" dentro de outro é chamado de "IF ANINHADO" e ocorre justamente 'quando eu tenho outra pergunta'
    # depois daquela feita anteriormente. Como se fosse "um bloco menor" dentro de outro "blobo maior".
    if num1 > num2:
        print(num1, "é maior que", num2)
    else:
        print(f"{num1} é menor que {num2}.")
else:
    print("Números iguais.")


""" Exemplo como no Problema 02 """
print("="*20, "02 :)")

# O "ELSE" sempre dispensa que você digite uma condição pra ele, porque ele já entende como sendo
# tudo de resto, aquilo que sobrou diferente daquilo que você já definiu antes no "IF"
media = 4     # Você pode mudar aqui pra testar! :D

if media >= 7:
    print("== Aprovado ==")
else:
    print("== Reprovado ==")


""" Exemplo como no Problema 03 """
print("="*20, "03 :)")

# O "ELIF" é como se fosse todas as outras condições quando tiverem mais de duas. É como se fosse
# " SE manhã, isso...    SE tarde, aquilo...     SE NÃO, aquilo outro "
if media >= 7:
    print("== Aprovado ==")
elif media >= 4:
    print("== Aluno em recuperação ==")
else:
    print("== Reprovado ==")


""" Exemplo como no Problema 05 """
print("="*20, "05 :)")

# A letra Maiúscula e a letra Minúscula são DIFERENTES pro programa, então se você quer receber as duas "como se
# fossem iguais", precisa deixar isso claro no "IF", então a escrita fica um pouco diferente de como tava sendo antes.

resposta = "S"     # Você pode mudar aqui pra testar! :D
if resposta in "Ss" or resposta in "Nn":
# Uso "OR" pq só precisa que PELO MENOS UMA seja verdadeira, e já entra nesse "IF"
    if resposta in "Ss":
        print("Foi sim.")
    else:
        print("Foi não.")
else:
    print("Não foi nem 'S' ou 's' nem foi 'N' ou 'n'!")


""" Exemplo com no Problema 06"""
print("="*20, "06 :)")

# Pra eu saber se o número é "par" eu só preciso saber que o resto da divisão desse número por "2" dá = "0",
# e pra isso utilizo o símbolo de resto "%"
if num1 % 2 == 0:
    print(f"{num1} é par.")
else:
    print(f"{num1} é ímpar.")

if num2 % 2 == 0:
    print(f"{num2} é par.")
else:
    print(f"{num2} é ímpar.")


""" Exemplo como no Problema 07"""
print("="*20, "07 :)")

# Para o uso do "AND", TUDO precisa ser verdade pra valer como "True" aquela afirmação.
if num1 > 1 and num1 < 4:
    print(F"1 é menor que {num1} que também é menor que 4")
else:
    print(f"{num1} é maior que 1, mas não é menor que 4!")
