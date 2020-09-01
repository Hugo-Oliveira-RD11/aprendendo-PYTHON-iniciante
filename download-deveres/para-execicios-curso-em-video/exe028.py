import random

print('eu estou pensando em um numero entre 0 e 5, e vc vai ter que acertar')
n = int(input('digite aqui seu chute:'))
print('PROCESSANDO...')
a = random.randint(0, 5)
if n == a:
    print('PERDI, parabens vc acertou!!')
else:
    print('GANHEI, vc errou, o numero era {}'.format(a))
