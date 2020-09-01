numero1 = int(input('digite o primeiro numero: ' ))
numero2 = int(input('digite o segundo numero: '))
s = numero1 + numero2
n = numero1 - numero2
d = numero1 / numero2
m = numero1 * numero2
di = numero1 // numero2
e = numero1 ** numero2
print('a soma e {}, a subtração e {},a multiplicação e {}, a divisão e ( resumida ) {:.4f}'.format(s, n, m, d), end='')
print('a divisão de numero inteiro e {},a potenciação e {}'.format(di, e))
print('divisao nao resumida: {}'.format(d))