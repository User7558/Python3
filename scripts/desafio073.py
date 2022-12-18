#Desafio 73: Melhore o DESAFIO 72, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
#
pa = int(input('Digite o primeiro termo da Progressão Aritmética: '))
r = int(input('Digite a razão da P.A.: '))
c = 0
total = 0
mais = 10

print('--' * 25)
print('\033[;49;34mMostrando os termos da Progressão Aritmética...\033[m')
print('--' * 25)

while mais != 0:
  total += mais
  while c <= total:
    print(pa, end=' -> ')
    pa += r
    c += 1
  print('PAUSA')
  mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Fim do programa.')
print(f'Progressão finalizada com {total} termos mostrados.')
