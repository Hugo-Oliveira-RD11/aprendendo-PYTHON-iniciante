nota1 = float(input('primeira nota :'))
nota2 = float(input('segunda nota :'))
media = (nota1 + nota2) / 2
print('tirando a nota {:.1f} e {:.1f} sua media e {:.1f}'.format(nota1, nota2, media))
if media >= 7:
    print('vc esta aprovado')
elif 7 > media >= 5:
    print('vc estar em recuperação')
else:
    print('vc estar reprovado')
