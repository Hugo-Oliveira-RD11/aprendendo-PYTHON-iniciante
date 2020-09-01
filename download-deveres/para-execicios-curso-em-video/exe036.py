casa = float(input('qual e o valor da casa que vc quer compra? R$'))
salario = float(input('quanto vc recebe por mes? R$'))
anos = float(input('em quantos anos vc vai pagar pela casa (prestação)? R$'))

c1 = (salario * 30 / 100)
c2 = casa / (anos * 12)

if c2 <= c1:
    print('para comprar a casa de R${} em {} anos, você pagarar R${:.2f}\ne sim!!,VOCÊ PODE COMPRAR A CASA'.format(casa,
                                                                                                                   anos,
                                                                                                                   c2))
elif c2 > c1:
    print(
        'para pegar uma casa de R${} em {}anos, você terar de pagar R${:.2f}\ne seu salario e muito pouco,'
        'SEU IMPRESTIMO FOI NEGADO'.format(
            casa, anos, c2))
