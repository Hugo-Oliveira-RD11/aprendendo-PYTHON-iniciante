nome = str(input('digite seu nome completo :')).strip()

caixaalta = nome.upper()
caixamenor = nome.lower()
semespaço = len(nome) - nome.count(' ')
pnome = nome.split()

print('seu nome em caixa alta e {}'.format(caixaalta))
print('seu nome em nimusculas e {}'.format(caixamenor))
print('seu nome sem espaço tem {}'.format(semespaço))
print('seu primeiro nome e {} e tem {} numeros'.format(pnome[0].capitalize(),len(pnome[0])))
