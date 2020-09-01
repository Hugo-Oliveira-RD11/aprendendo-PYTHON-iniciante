times = ['internacional', 'vasco', 'atletico-MG', 'palmeiras', 'são paulo'
         , 'santos', 'fluminence', 'bahia', 'grêmio', 'Atletico-PR', 'botafogo', 'bragantino'
         , 'flamengo', 'corinthias', 'goias', 'fortalesa', 'atletico-GO', 'sport', 'ceara', 'coritiba']
print(f'lista de times do brasileirão de 2020 : {times}')
print('='*35)
print(f'os cincos primeiros : {times[:5]}')
print('='*35)
print(f'os quatros ultimos : {times[16:]}')
print('='*35)
print(f'em ordem alfabetica : {sorted(times)}')
print('='*35)
print(f'e o corinthias estar em {times.index("corinthias")+1}° posição')
