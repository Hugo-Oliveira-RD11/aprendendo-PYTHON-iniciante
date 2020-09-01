maiores = 0
homem = 0
mulher = 0
while True:
    sexo = ' '
    opc = ' '
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('idade :'))
    while sexo not in 'MF':
        sexo = str(input('sexo :[ M / F ]')).strip().upper()
    while opc not in 'SNsn':
        opc = str(input('quer continuar [ S / N ] :')).strip().upper()
    if idade >= 18:
        maiores += 1
    if sexo in 'M':
        homem += 1
    if sexo in 'F':
        if idade < 20:
            mulher += 1
    if opc in 'Nn':
        break
print('total de pessoas com mais de 18 anos = {}'.format(maiores))
print('Ao todo temos {} homem'.format(homem))
print('E temos {} mulher com menos de 20 anos'.format(mulher))
