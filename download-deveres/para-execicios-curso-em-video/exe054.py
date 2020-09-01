from datetime import date
soma1 = 0
soma2 = 0
atual = date.today().year
for c in range(1, 7+1):
    naci = int(input('nacimento da {}º pessoa'.format(c)))
    c1ano = atual - naci
    if c1ano <= 21:
        soma1 += 1
    else:
        soma2 += 1
print('de 7 pessoas, {} sao MAIORES DE IDADE\ne {} SAO MENORES DE IDADE'.format(soma1, soma2))
