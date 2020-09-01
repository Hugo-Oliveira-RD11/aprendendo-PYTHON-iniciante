import random
p = input('primeiro aluno :')
s = input('segundo aluno :')
t = input('terceiro aluno :')
q = input('quarto aluno :')

lista = [p, s, t, q]
random.shuffle(lista)

print(lista)
