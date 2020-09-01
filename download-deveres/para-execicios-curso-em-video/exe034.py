s = float(input('digite o salario do funcionario? R$'))

if s <= 1250.0:
    c1 = (s * 15 / 100) + s
    print('agora o funcionario vai ter o reajuste de 15%\nentao o salario dele que era R${:.2f}, passa a ser de R${:.2f}'.format(s, c1))
else:
    c2 = (s * 10 / 100) + s
    print('agora o fucionario vai ter o reajuste de 10%\nentao o salario dele que era R${:.2f}, passa a ser de R${:.2f}'.format(s, c2))
