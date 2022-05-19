#desafio31: desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km e R$0.45 para viagens mais longas
#
km = int(input('Qual a distância da viagem (em quilômetros)? '))
if (km <= 200):
    v = km*0.50
    print('O preço da passagem será de R${:.2f}'.format(v))
else:
    v = km*0.45
    print('O preço da passagem será de R${:.2f}'.format(v))

#SIMPLIFICADO: v = km*0.50 if km<=200 else v = km*0.45