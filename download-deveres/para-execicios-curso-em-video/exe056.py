from time import sleep
conta = 0
contaidade = 0

for pessoas in range(1, 5):
    print('-' * 10, end='')
    print('{}° PESSOA'.format(pessoas), end='')
    print('-' * 10)
    nome = input('qual e o seu nome :')
    idade = int(input('qual e a sua idade :'))
    sexo = input('qual e o seu sexo ( F / M ):').lower()
    maior = idade
    if pessoas == 1 and sexo == 'm':
        maisvelho = nome
        maisvelho2 = idade
    elif sexo == 'm':
        if maisvelho2 < idade:
            maisvelho2 = idade
            maisvelho = nome
    elif sexo == 'f':
        if idade < 20:
            conta += 1
    if pessoas == 1:
        idade1 = idade
    elif pessoas == 2:
        idade2 = idade
    elif pessoas == 3:
        idade3 = idade
    elif pessoas == 4:
        idade4 = idade

mediaidade= (idade1 + idade2 + idade3 + idade4) / 4
print('ANALISANDO DADOS...')
sleep(2)
print('a MEDIA DE IDADE do grupo e de {:.1f}'.format(mediaidade))
sleep(0.5)
print('o HOMEM MAIS VELHO tem {} anos e se chama {}'.format(maisvelho2, maisvelho.capitalize()))
sleep(0.5)
print('ao todo são {} MULHERES COM MENOS DE 20 anos'.format(conta))
