n = float(input('digite o preço do produto R$'))
d = n * 5 / 100
r = n - d
print ('o produto que antes custava {}R$, agora custa {:.2f}R$'.format(n, r))
