from time import sleep
print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
sleep(0.5)
pt = int(input('primeiro termo :'))
sleep(0.2)
pt2 = int(input('segundo termo :'))
sleep(0.2)
zero = pt + (10 - 1) * pt2

for c in range(pt, zero + pt2, pt2):
    print(c, end=' ',)
print('acabou')
