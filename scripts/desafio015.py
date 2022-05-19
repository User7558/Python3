#desafio15: um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado
#
km=float(input('Quantos km o carro alugado percorreu? '))
d=int(input('Por quantos dias ele foi alugado? '))
a = (60*d)+(0.15*km)
print('O preço que deverá ser pago pelo aluguel do carro será de R${:.2f}.'.format(a))
