num = int(input('digite um numero entre 0 e 20 :'))
if num < 0 or num > 20:
    while True:
        num = int(input('digite um numero :'))
        if num > 0 and num < 20:
            break
extenco = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'trese', 'quatoze', 'quinze', 'deseceis', 'desesete', 'desoito', 'desenove', 'vinte']
print(f'vc digitou o numero {extenco[num]}')
