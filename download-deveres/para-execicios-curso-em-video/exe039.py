from datetime import date

nacimento = int(input('em que ano vc nasceu ?'))

if nacimento + 18 < date.today().year:
    cnascimento = date.today().year - nacimento
    calistamento = cnascimento - 18
    calculoano = date.today().year - calistamento
    print('voce nasceu em {} e tem {} anos em {}'.format(nacimento, cnascimento, date.today().year))
    print('vc ja deveria ter se alistado em {} anos'.format(calistamento))
    print('seu alistamento foi em {}'.format(calculoano))

elif date.today().year - nacimento == 18:
    cnacimento = date.today().year - nacimento
    print('VOCÊ TEM QUE SE ALISTAR IMEDIATAMENTE')
    print('vc nasceu em {} e tem {} anos em {}'.format(nacimento, cnacimento, date.today().year))

elif nacimento + 18 > date.today().year:
    cnascimento = date.today().year - nacimento
    calistamento = 18 - cnascimento
    ano = date.today().year + calistamento
    print('vc nasceu em {} e tem {} anos em {}'.format(nacimento, cnascimento, date.today().year))
    print('falta {} anos, para vc se alistar'.format(calistamento))
    print('seu alistamento vai ser em {}'.format(ano))
