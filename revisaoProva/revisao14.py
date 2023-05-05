# Revisao 14:

# Escreva um algoritmo para ler uma temperatura em graus Fahrenheit. Calcular e escrever o valor correspondente
# em graus Celsius (baseado na fórmula abaixo):
# C = ((F - 32)/9)*5
# Observação: Para testar se a sua resposta está correta saiba que 100 ⍛C = 212 F

temp = float(input("Temperatura (em ºF): "))

cels = ((temp - 32)/9)*5

print(f"{temp}ºF = {cels}ºC")
