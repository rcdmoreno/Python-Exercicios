def encontrar_num_par(x):
    if x % 2 == 0:
        print('Este numero é par: ', x)
    else:
        print('Este numero é impar: ', x)

print('Encontrar o Número Par!!')
num = int(input('Digite um numero: '))

encontrar_num_par(num)
