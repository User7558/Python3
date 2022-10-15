#Desafio066: Faça um programa que leia o peso de 5 pessoas. no final, mostre qual foi o maior e o menor peso lidos.
#
menor = 0
maior = 0

for c in range (0,5):
  peso = float(input(f'Insira o peso (em kg) da {c+1}ª pessoa: '))
  if c==1:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    elif peso < menor:
      menor = peso

print(f'Menor peso registrado: {menor}kg.')
print(f'Maior peso registrado: {maior}kg.')
