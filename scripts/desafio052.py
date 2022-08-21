'''Desafio052: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
-se ele ainda vai se alistar ao serviço militar (-18)
-se já é a hora de se alistar (18)
-se já passou do tempo de alistamento (+18)
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
#
from datetime import date 

an = int(input('Em qual ano você nasceu: '))
at = date.today().year
i = at - an 

print(f'Atualmente você possui {i} anos...')
if i < 18:
  f = 18 - i 
  print(f'Você deverá se alistar no exército daqui {f} anos.')
elif i == 18:
  print('É sua hora de se alistar no exército')
else:
  f = i - 18 
  print(f'Seu alistamento esta atrasado em {f} anos.')
