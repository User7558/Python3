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
  n = str(input('Informe seu nome: '))
  g = int(input('''Qual seu gênero? 
  [1] Mulher
  [2] Homem
  *--------------* 
  R: '''))
  i = int(input('Qual sua idade? '))
  print('-='*20)
  if i > midade and g == 2:
    midade = i
    nome = n
  elif i < 20 and g == 1:
    menor += 1
  media += i
media = media/4

print(f'Média de idade: {media:.2f}.')
print(f'Nome do homem mais velho: {nome}.')
print(f'Quantidade de mulheres que tem menos de 20 anos: {menor}.')
