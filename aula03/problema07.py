# Problema 07:

# Receba um número de 1 a 12 e mostre o nome do mês correspondente. Caso o mês não
# exista, mostrar essa informação. Obs.: usando IF

numero = int(input("Digite um número de 1 a 12: \n"))

if numero >= 1 and numero <= 12:     # No uso do "AND", AS DUAS condições precisam ser "V" pra tudo valer também.
    if numero <= 4:
        if numero == 1:
            print(f"{numero} é o mês de janeiro.")
        elif numero == 2:
            print(f"{numero} é o mês de fevereiro.")
        elif numero == 3:
            print(f"{numero} é o mês de março.")
        else:
            print(f"{numero} é o mês de abril.")
    elif numero <= 8:     # Não preciso definir até "4" porque já tá definido no "IF" anterior.
        if numero == 5:
            print(f"{numero} é o mês de maio.")
        elif numero == 6:
            print(f"{numero} é o mês de junho.")
        elif numero == 7:
            print(f"{numero} é o mês de julho.")
        else:
            print(f"{numero} é o mês de agosto.")
    else:     # Aqui ele só vai considerar o que tá faltando acontecer dentro do "IF" aninhado do qual pertence.
        if numero == 9:
            print(f"{numero} é o mês de setembro.")
        elif numero == 10:
            print(f"{numero} é o mês de outubro.")
        elif numero == 11:
            print(f"{numero} é o mês de novembro.")
        else:
            print(f"{numero} é o mês de dezembro.")
else:
    print("Número inválido!")


# Ao invés de considerar os números entre 1 e 12 como um bloco só, eu dividi em 4 partes pra diminuir a quantidade
# de processamentos que o computador vai fazer! Porque, por exemplo, considerando "o pior dos casos", se aparece pra
# mim o mês "12", "dezembro", ele vai analisar:
#       " está entre 1 e 12! / é 1? / é 2? / é 3? / é 4? / é 5? / é 6? / é 7? / é 8? / é 9? / é 10? / é 11? / é 12! "
#                                      ELE FEZ --13-- CONFERÊNCIAS!
# Com a divisão de análise que eu coloquei, vai ficar no máximo assim:
#       " está entre 1 e 12! / está de 1 a 4? / de 5 a 8? / de 9 a 12! / é 9? / é 10? / é 11? / é 12! "
#                                   ELE FEZ APENAS --8-- CONFERÊNCIAS!
