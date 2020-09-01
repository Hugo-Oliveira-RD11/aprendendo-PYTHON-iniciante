dia = int(input('quantos dias vc andou nele? '))
kilometros = float(input('quantos quilometros vc andou nele? '))

total = (dia * 60) + (kilometros * 0.15)

print('total a pagar {:.2f}'.format(total))
