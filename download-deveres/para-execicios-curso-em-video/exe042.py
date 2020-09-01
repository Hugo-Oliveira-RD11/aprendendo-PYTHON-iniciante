lado1 = float(input('digite o primeiro lado do tringulo :'))
lado2 = float(input('digite o segundo lado :'))
lado3 = float(input('digite o terceiro lado :'))

if lado1 + lado2 >= lado3 and lado2 + lado3 >= lado1 and lado1 + lado3 >= lado2:
    print('esses numeros podem SIM!! forma um triangulo',end='')

    if lado1 == lado2 == lado3:
        print('esse triangulo e equilotero!!')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('esse triangulo e ísoscelis')
    else:
        print('esse tringulo e escaleno')

else:
    print('esse numeros não podem forma um triangulo!!')
