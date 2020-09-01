print('=' * 10, end='')
print('BUTECO', end='')
print('=' * 10)

dindi = float(input('quanto custou a compra? R$'))
print('[ 1 ] DINHEIRO/CHEQUE\n[ 2 ] CARTÃO (a vista)\n[ 3 ] ATÉ 2x NO CARTÃO\n[ 4 ]3x OU MAIS NO CARTÃO')
escolha = int(input('qual e a sua escolha?'))

if escolha == 1:
    desc = dindi * 10 / 100
    aplicar = dindi - desc
    print('sua compra que era de R${:.2f}, passa a ser R${:.2f}'.format(dindi, aplicar))
elif escolha == 2:
    desc = dindi * 5 / 100
    aplicar = dindi - desc
    print('pagando no cartão a vista, sua compra que era de R${:.2f}, passa a ser R${:.2f}'.format(dindi, aplicar))
elif escolha == 3:
    parcela = dindi / 2
    print('pagando em 2x, vc vai ter que pagar em R${:.2f} por dois meses'.format(parcela))
elif escolha == 4:
    parcela = int(input('vc quer parcelar por quantos meses ?'))
    sjuros = dindi * 20 / 100
    juros = (sjuros + dindi) / parcela
    juros2 = juros + dindi
    print('sua compra sera parcelada em {}x de R${} COM JUROS'.format(parcela, juros))
    print('entao oque era R${:.2f} agora e R${:.2f}'.format(dindi, juros2))
else:
    print('por favor reinicie o software, e coloque uma das opções.')
