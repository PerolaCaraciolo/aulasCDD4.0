# Revisão 11:

# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa
# expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

print("Digite sua data de nascimento em números: ")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

diasHoje = 4 + (4 * 30) + (2022 * 365)     # Quantidade total de dias até o dia de hoje.

diasNasc = dia + ((mes-1)*30) + ((ano-1)*365)     # Quantidade total de dias até o dia do seu nascimento.

print(f"Sua idade em dias até hoje: {diasHoje - diasNasc} dias.")

# Pra saber a idade a gente geralmente diminui o ano atual pelo de nascimento. Se for pra considerar em dias, eu já
# faço esse cálculo em dias desde o início.

# Eu diminuo o ano em 1 pois o atual vai estar incluído nos meses e dias, já que não posso contar com ele completo.
# Eu diminuo o mês em 1 pelo menos motivo, o atual vai estar em dias. Ele ainda está sendo decorrido, não completo.
# Os dias entram normais.



             # COMO O PROFESSOR FEZ (ele considerou que o próprio usuário ia dizer certinho cada cálculo):
"""
anoP = int(input("Digite os anos da sua idade: "))
mesP = int(input("Digite os meses da sua idade: "))
diaP = int(input("Digite os dias da sua vida: "))

print(anoP*365+mesP*30+diaP)
"""