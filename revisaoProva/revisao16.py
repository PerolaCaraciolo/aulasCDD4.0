# Revisão 16:

# Escreva um algoritmo para ler a hora de início e a hora de fim de um jogo de Xadrez (considere apenas horas
# inteiras, sem os minutos) e calcule a duração do jogo em horas, sabendo-se que o tempo máximo de duração do jogo
# é de 24 horas e que o jogo pode iniciar em um dia e terminar no dia seguinte.

horaInicio = int(input("Hora início do jogo: "))
horaFim = int(input("Hora fim do jogo: "))

if horaFim < horaInicio:
    duracao = (horaFim - horaInicio) + 24
elif horaFim > horaInicio:
    duracao = horaFim - horaInicio
else:
    duracao = (horaFim - horaInicio) + 24
    print("Tempo de duração: 0h \n  OU")

print(f"Tempo de duração: {duracao}h")
