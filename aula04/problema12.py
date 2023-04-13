# Problema 12:

# Ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10,20] (incluindo os
# valores 10 e 20 no intervalo) e quantos deles estão fora deste intervalo.

intervalo = 0
foraIntervalo = 0

for num in range(10):
    valores = int(input("Digite um número inteiro acima de '0': "))
    if 10 <= valores <= 20:
        intervalo += 1
    else:
        foraIntervalo +=1

print(f"Você digitou: \n{intervalo} valor(es) no intervalo de 10 até 20. \n{foraIntervalo} fora desse intervalo.")
