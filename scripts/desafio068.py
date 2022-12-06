#Desafio 68: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
#
nome = str(input('Digite seu nome: '))
sexo = ''
check = False

while check == False:
  sexo = str(input('Qual seu gênero? [F/M] ')).upper()
  if sexo == 'F' or sexo == 'M':
    check = True
  else:
    print('Por favor, tente novamente. (Respostas aceitas: [F/M])')
    
if sexo == 'F':
  print(f'Olá {nome}, seja bem-vinda!')
elif sexo == 'M':
  print(f'Olá {nome}, seja bem-vindo!')
