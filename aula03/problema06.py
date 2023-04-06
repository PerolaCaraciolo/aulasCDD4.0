# Problema 06:

# Receba um número do usuário e diga se ele é par ou ímpar. Considere "0" como inválido.

numero = float(input("Digite um número: "))

if numero != 0:     # Mesmo raciocínio do Problema 01.
    if numero % 2 == 0:     # Pra eu saber se o número é par, considero o resto de sua divisão por "2" como = "0".
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
else:
    print("Número inválido.")
