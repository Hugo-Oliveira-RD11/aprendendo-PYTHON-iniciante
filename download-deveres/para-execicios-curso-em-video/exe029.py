carro = int(input('digite a velocidade do carro :'))

if carro < 80:
    print('parabens, voce estar dentro da lei!!!')
    print('tenha um bom dia!!')

if carro == 80:
    print('tome CUIDADO!!\npois o LIMITE DE VELOCIDADE e de 80 KM/h\nse vc passar disso e multa de R$7,00 por quilometro')
    print('tenha um bom dia, E DIRIJA COM CUIDADO!!')

else:
    c = (carro - 80) * 7
    print('vc estar mandando muito MAL\no LIMITE DE VELOCIDADE e de 80KM/h\na sua multa e de R${:.2f}'.format(c))
    print('bom dia, DIRIJA COM SEGURANÇA')
