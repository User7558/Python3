#desafio045: Faça um programa que leia as duas notas de uma quantidade indeterminada de alunos e indique se cada um deles foi aprovado ou reprovado se a média das notas for maior que 5 e, ao final, apenas imprima as quantidades de aprovados e de reprovados.
#
al = 0
ap = 0
rep = 0
r = ''

while r != 'n':
  n1=int(input('Nota da primeira prova: '))
  n2=int(input('Nota da segunda prova: '))
  m = (n1+n2)/2
  if m > 5:
    ap += 1
  else:
    rep += 1
  r=str(input('Deseja inserir mais um(a) aluno(a)? [S/N] ')).lower()
print(f'''Total de alunos: {al} 
Total de alunos aprovados: {ap}
Total de alunos reprovados: {rep}''')
