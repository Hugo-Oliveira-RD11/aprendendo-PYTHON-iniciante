nada = 3
num = 0
num2 = 1
num3 = 0
opcao = int(input('quantos termos vc quer mostras ?'))
print(num, num2, end='')
while not opcao == nada:
    num3 = num + num2
    print(' ', num3, end='')
    num = num2
    num2 = num3
    nada += 1
