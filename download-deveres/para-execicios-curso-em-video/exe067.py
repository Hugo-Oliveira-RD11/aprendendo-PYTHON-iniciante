from time import sleep
while True:
    opc = int(input('digite do numero para ver a tabuada dele :'))
    if opc <0:
        break
    sleep(0.3)
    print('-'* 42)
    for c in range(1,11):
        print(f'{opc} x {c} = {opc * c}')
    print('-'* 42)
    sleep(0.5)
print('obrigado por usar esse programa\nVOLTE SEMPRE!!')
