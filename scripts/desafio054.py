'''Desafio054: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- abaixo de 18.5: abaixo do peso
- enter 18.5 e 25: peso ideal
- 25 até 30: sobre peso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida'''
#
peso = float(input('Qual seu peso (kg)? '))
alt = float(input('Qual sua altura (cm)? '))
imc = peso/(alt)**2

if imc<18.5:
  print(f'Seu IMC é {imc:.2f}, você está \033[1;34mabaixo\033[m do peso ideal.')
elif imc>=18.5 and imc<=25:
  print(f'Seu IMC é {imc:.2f}, você está no \033[1;32mpeso ideal\033[m.')
elif imc>=25 and imc<=30:
  print(f'Seu IMC é {imc:.2f}, você está em estado de \033[1;35msobrepeso\033[m.')
elif imc>=30 and imc<=40:
  print(f'Seu IMC é {imc:.2f}, você está em estado de \033[1;33mobesidade\033[m.')
else:
  print(f'Seu IMC é {imc:.2f}, você está em estado de \033[1;31mobesidade mórbida\033[m.')
