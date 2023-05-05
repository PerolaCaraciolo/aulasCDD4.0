# Revisão 04:

# Crie um algoritmo que receba 3 números e informe qual o maior entre eles.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

if n3 < n1 > n2:
    print(f"{n1} {n2} {n3} \n{n1} é o maior dos números.")
elif n3 < n2 > n1:
    print(f"{n1} {n2} {n3} \n{n2} é o maior dos números.")
else:
    print(f"{n1} {n2} {n3} \n{n3} é o maior dos números.")
