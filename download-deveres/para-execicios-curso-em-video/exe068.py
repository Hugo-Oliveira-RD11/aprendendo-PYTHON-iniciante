from random import randint
from time import sleep
print('=-' * 13)
print('VAMOS JOGAR IMPAR OU PAR')
print('=-' * 13)
soma = 0
conta = 0
sleep(0.2)
while True:
    aleatorio = randint(1, 10)
    player = int(input('qual numero vc escolhe ?'))
    opc = str(input('vc quer impar ou par ? [ I / P ]').strip())
    soma = player + aleatorio
    print('vc jogou {} e o computador jogou {},'.format(player, aleatorio), end='')
    if opc in'iIimparIMPARImpar':
        if soma % 2 == 0:
            print(f'Total de {soma}, deu PAR')
            print('Você PERDEUUUU!!')
            break
        elif soma % 2 == 1:
            print(f'Total de {soma}, deu IMPAR')
            print('Você GANHOUUU!!')
            conta += 1
    elif opc in 'pPparPARPar':
        if soma % 2 == 0:
            print(f'Total de {soma}, deu PAR')
            print('Você GANHOUUUU!!\nvamos jogar novamente...')
            conta += 1
        elif soma % 2 == 1:
            print(f'Total de {soma}, deu IMPAR')
            print('Você PERDEUUUU!!')
            break
print('GAME OVER, você venceu {} veses'.format(conta))
