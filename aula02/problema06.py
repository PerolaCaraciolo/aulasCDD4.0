# Problema 06:

# Duas variáveis (A e B) possuem valores distintos (A=5 e B= 10). Crie um algoritmo que armazene esses
# dois valores nessas duas variáveis e efetue a troca dos valores de forma que a variável A passe a
# possuir o valor da variável B e que a variável B passe a possuir o valor da variável A.
# Por fim, apresentar os valores trocados.

a = 5
b = 10
print(f"Valores iniciais: a = {a} e b = {b}")

a1 = a    # Essa variável foi criada como uma "auxiliar", só pra possibilitar que o valor original seja guardado
          # pra utilizar depois.

a = b    # No momento em que eu adiciono outro valor a uma variável já criada anteriormente, ela assume esse novo valor.
b = a1
print(f"Valores invertidos: a = {a} e b = {b}")
