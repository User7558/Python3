#Desafio 69: Melhore o jogo do DESAFIO 28, onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vaitentar adivinhar até acertar, mostrando no final quantos palputes foram necessários para vencer.
#
from random import randint
from time import sleep

print('JOGO DA ADVINHAÇÃO V2.0')
print('-' * 30)

j = int(input('Digite um número de 0 a 10: '))
pc = randint(0,10)
tentativas = 1

print('Processando...')
sleep(1)

while j != pc:
  j = int(input('Errado! Vamos lá, tente novamente: '))
  print('Processando...')
  sleep(0.5)
  tentativas += 1
  if pc == j:
      print(f'Parabéns, você venceu o jogo da adivinhação, e para isso precisou de {tentativas} tentativas!')
  elif pc == j and tentativas == 1:
      print('Um vidente! Você venceu o jogo da adivinhação, e para isso precisou de apenas uma tentativa!')
