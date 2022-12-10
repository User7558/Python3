#Desafio 73: Melhore o DESAFIO 72, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
#
pa = int(input('Digite o primeiro termo da Progressão Aritmética: '))
r = int(input('Digite a razão da P.A.: '))
t = 12
usuario = 1

print('-=' * 25)
print('\033[;49;34mMostrando os termos da Progressão Aritmética...\033[m')

while usuario != 0:
  print(pa, end=' -> ')
  pa += r
  t -= 1
  if t == usuario:
    usuario = int(input('Quantos termos quer mostrar? '))

print('Fim do programa.')
#para corrigir