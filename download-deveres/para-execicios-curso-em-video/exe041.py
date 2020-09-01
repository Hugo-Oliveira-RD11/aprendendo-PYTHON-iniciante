from datetime import date
nacimento = int(input('digite sua data de nacimento :'))
atual = date.today().year
idade = atual - nacimento
print('o atleta tem {} anos'.format(idade))
if idade <= 9:
    print('sua categoria e MIRIM')
elif 9 < idade <= 14:
    print('sua categoria e INFANTIL')
elif 14 < idade <= 19:
    print('sua categoria e JÚNIOR')
elif 19 < idade <= 25:
    print('sua categoria e SÊNIOR')
else:
    print('sua categoria e MASTER')
