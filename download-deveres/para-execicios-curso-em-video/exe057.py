s = str(input('digite o seu sexo [ M / F ] :'))
if s == 'm' or s == 'f':
    print('DADOS GUARDADOS\nobrigado pela paciencia, tenha um bom dia')
else:
    m = 'm'
    f = 'f'
    s2 = 0
    while s2 != m and s2 != f:
        s2 = input('por favor digite seu sexo [ M / F ] :')
    print('DADOS GUARDADOS\nobrigado pela sua paciencia...')
