n1 = float(input('qual e a largura da sua parede :'))
n2 = float(input('qual e a comprimento da sua parede :'))
l = n1 * n2
p = l / 2
print('sua parede tem a dimesao de {}x{} é sua area no total e de {:.3f}m²'.format(n1, n2, l))
print(' a tinta que vc tem que gasta para coprir toda a parede é {}l'.format(p))