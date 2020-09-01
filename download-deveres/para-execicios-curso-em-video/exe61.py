conta = 0
n1 = int(input('primeiro termo :'))
n2 = int(input('razão PA :'))
print(n1, end=' ')
while not conta == 10:
    conta += 1
    n1 += n2
    print(n1, end=" ")
print('\nse n quiser mostrar mais nada e so digitar 0')
pergunta1 = 1
while not pergunta1 == 0:
    pergunta1 = int(input('\nvc quer mostrar mais quantas razoes ?'))
    if not pergunta1 == 0:
        zero = n1 + (pergunta1 - 1) * n2
        for c in range(n1, zero + n2, n2):
            print(c, end=' ')
if pergunta1 == 0:
    print('progresso finalizado com sucesso!')
