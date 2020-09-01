print('digite 1 para masculino e 0 para feminino.')
sexo = int(input('qual e o seu sexo? (numero)'))

if sexo == 1:
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

elif sexo == 0:
    print('vc n precisa se alistar!!\nmas se quiser e so digitar 1 pra sim e 0 pra não')
    quero = int(input('voce quer saber quando vai querer se alisatar ?'))

    if quero == 1:
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

    elif quero == 0:
        print('tenha um bom dia!')
    else:
        print('por favor reinicie o programa e digite um numero entre 0 e 1')

else:
    print('por favor reinicie o programa e digite um numero entre 0 e 1')
