frase = str(input('digite uma frase :')).strip()

d = frase.lower()
cm = d.count('a')
cma = d.find('a') + 1
cma2 = d.rfind('a') + 1

print('a sua frase tem {} A'.format(cm))
print('o primeiro A da sua frase começa {}'.format(cma))
print('o ultimo A da sua frase estar {}'.format(cma2))
