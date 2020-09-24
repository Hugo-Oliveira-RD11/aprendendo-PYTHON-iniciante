
def contar(* n):
    soma = 0
    for c in n:
        soma += c
    print(soma)

nun = int(input('quantos numeros vc quer somar :'))
for c in range(0,nun):
    nun2=int(input('digite os numeros para a soma :'))

contar(nun2)