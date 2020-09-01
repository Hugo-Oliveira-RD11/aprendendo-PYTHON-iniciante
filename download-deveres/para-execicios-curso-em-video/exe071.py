print('=' * 25)
print('BANCO PARA RICOS!!')
print('se você pobre sai agora!!')
dinheiro = int(input('quanto que vc quer sacar R$'))
tudo = dinheiro
dinheirop = 50
contagemc = 1
while True:
    if tudo >= dinheirop:
        tudo -= dinheirop
        contagemc += 1
    else:
        print('o total de {} celulas R${}'.format(contagemc, dinheirop))
        if dinheirop == 50:
            dinheirop = 20
        if dinheirop == 20:
            dinheirop = 10
        if dinheirop == 10:
            dinheirop = 1
        contagemc = 0
        if tudo == 0:
            break
