print('-=' * 12)
print('analizador de triagulos')
print('-=' * 12)

s1 = float(input('primeiro segmento :'))
s2 = float(input('segundo segmento :'))
s3 = float(input('terceiro segmento :'))

if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print('o seguimento acima PODE FORMA UM TRIANGULO!!')
else:
    print('o seguimento acima NÃO PODE FORMA UM TRIANGULO!!')
