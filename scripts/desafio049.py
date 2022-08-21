'''desafio050: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa deve perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
   Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.'''
#
print('\033[;93m='*40)
print('CENTRAL DE EMPRÉSTIMOS')
print('='*40)
print('\033[mBoas-vindas! Para analisar seu empréstimo, precisamos de algumas informações. Por favor nos informe...')

casa = float(input('O valor do imóvel que deseja comprar: R$'))
sal = float(input('O salário atual do comprador do imóvel: R$'))
ano = int(input('Em quantos anos pretende quitar seu empréstimo: '))

emp = casa / (ano*12)
mi = sal*30 / 100

if mi < emp:
  print ('Por exceder o valor de 30% do seu salário, seu empréstimo foi \033[1;31mnegado\033[m.')
else:
  print(f'Por estar dentro do limite, seu empréstimo de R${casa:.2f} foi \033[1;32maceito\033[m.')
