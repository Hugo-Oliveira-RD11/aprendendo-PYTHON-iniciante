cidade = str(input('qual cidade vc nasceu :')).strip()

m = cidade.lower()
d = m.split()
santo = 'santo' in d[0]

print(santo)
