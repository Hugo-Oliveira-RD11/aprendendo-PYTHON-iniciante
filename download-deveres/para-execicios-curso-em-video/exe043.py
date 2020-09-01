peso = float(input('qual e o seu peso? (kg)'))
altura = float(input('qual e a sua altura? '))
imc = peso / (altura * altura)
print('seu indici de gordura corpocal e de {:.1f}'.format(imc))
if imc <= 18.5:
    print('vc estar abaixo do peso!')
elif imc <= 24.9:
    print('vc estar com seu peso normal')
elif imc <= 29.9:
    print('vc estar com sobre peso!')
elif imc <= 39.9:
    if imc >= 30 and imc <= 34.9:
        print('vc estar no primeiro gral de obsidade')
    elif imc >= 35 and imc <= 39.9:
        print('vc estar no segundo gral de obsidade')
else:
    print('vc estar com obsidade morbida')
    print('JESUS')
