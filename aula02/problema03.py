# Problema 03:

# Faça um programa para calcular a média de 2 notas e mostrar essa média e o nome do aluno.

nome = input("Digite seu nome: ")
nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))    # Uso "FLOAT" antes do "INPUT" pq vou usar esse dado numa divisão
                                                    # em outro momento, então daria erro se não definisse o tipo de dado
                                                    # como numérico, já que ele consideraria como um texto normalmente.
media = (nota1 + nota2)/2

print(f"{nome}, sua média foi {media}.")     # Usando o comando "f" antes da impressão, possibilita só ir
                                            # adicionando as variáveis desejadas no local exato em que deseja com
                                            # com mais facilidade. Dentro de { }, como no exemplo.
