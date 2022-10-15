'''Desafio067: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre:
 - A média de idade;
 - Qual é o nome do HOMEM mais velho;
 - Quantas mulheres tem MENOS de 20 anos.'''
 #
media = 0 
nome = ''
midade = 0
menor = 0

for c in range (0,4):
  print(f'~ {c+1}ª Pessoa ~')
  n = str(input('Informe seu nome: '))
  g = str(input('Qual seu gênero? [F/M] ')).lower()
  i = int(input('Qual sua idade? '))
  print('-='*20)
  if i > midade and g == 'm':
    midade = i
    nome = n
  elif i < 20 and g == 'f':
    menor += 1
  media += i
media = media/4

print(f'Média de idade: {media:.2f}.')
print(f'O homem mais velho se chama {nome}, e possui {midade} anos.')
print(f'Quantidade de mulheres que tem menos de 20 anos: {menor}.')
