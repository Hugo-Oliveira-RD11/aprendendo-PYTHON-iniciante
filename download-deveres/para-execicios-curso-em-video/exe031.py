v = float(input('digite a distancia da sua viagem :'))

if v <= 200:
    c1 = v * 0.50
    print('a taxa de cobrança e de R$0,50')
    print('sua viagem vai ser de R${:.2f}'.format(c1))

else:
    c2 = v * 0.45
    print('a taxa acima de 200KM/h, e de R$0,45')
    print('entao sua viagem vai ser de R${:.2f}'.format(c2))
