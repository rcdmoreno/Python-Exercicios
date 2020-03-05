num = int(input('Digite um numero: '))

x = 0
while x <= num:
    if x % 2 == 0:
        print('Este numero é par: ', x)
    else:
        print('Este numero é impar: ', x)
    x += 1