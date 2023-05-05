# Revisão 12:

# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos.
# Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

eleitores = int(input("Digite o número de eleitores: "))
brancos = int(input("Votos bracos: "))
nulos = int(input("Votos nulos: "))
validos = int(input("Votos válidos: "))

branPerc = (100*brancos)/eleitores
nulPerc = (100*nulos)/eleitores
valPerc = (100*validos)/eleitores

print(f"\nTotal de eleitores: {eleitores} \nBrancos: {branPerc}% \nNulos: {nulPerc}% \nVálidos: {valPerc}%")
