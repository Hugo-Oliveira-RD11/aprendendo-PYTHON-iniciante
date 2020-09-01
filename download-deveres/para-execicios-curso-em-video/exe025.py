nome = str(input('digite seu nome completo :')).strip()
m = nome.lower()
d = m.split()
silva = 'silva' in d
print('seu nome tem ?{}'.format(silva))
