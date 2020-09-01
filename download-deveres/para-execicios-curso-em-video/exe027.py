nome = str(input('digite seu nome completo :')).strip()

n = nome.split()

print('prazer em te conhecer!! {}'.format(nome.split()[0].capitalize()))
print('seu primeiro nome e {}'.format(nome.split()[0].capitalize()))
print('seu ultimo nome e {}'.format(n[len(n) - 1].capitalize()))

#eu colei so um pouco na ultima