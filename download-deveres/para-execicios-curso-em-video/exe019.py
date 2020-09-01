import random
p = str(input('digite o nome do primeiro aluno :'))
s = str(input('o nome do segundo aluno :'))
t = str(input('o nome do terceiro aluno :'))
q = str(input('o nome do quato aluno :'))

lista = [p, s, t, q]
aluno = random.choice(lista)
print('o aluno sorteado foi {}'.format(aluno))
