print('-'*20)
print('LOJA SUPER BARATONA')
print('-'*20)
compra = 0
maiormil = 0
conta = 0
while True:
    conta += 1
    opc = ' '
    produto = input('nome do produto :')
    preco = float(input('preço do produto R$'))
    while opc not in 'SNsn':
        opc = str(input('quer continuar [ S / N ] :'))
    compra += preco
    if preco >= 1000:
        maiormil += 1
    if conta == 1:
        menor = preco
        nomemenor = produto
    if menor > preco:
        menor = preco
        nomemenor = produto
    if opc in 'Nn':
        break
print('--------------FIM DO PROGRAMA--------------')
print('O Total da compra foi de R${:.2f}'.format(compra))
print(f'temos {maiormil} produtos custando mais de R$1.000')
print('O produto mais barato foi {} que custa R${}'.format(nomemenor, menor))
