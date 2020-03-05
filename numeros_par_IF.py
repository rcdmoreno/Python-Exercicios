## outra forma de conseguir os numeros pares, mundando o incremento de 2 em 2 e contador 0 por que pe é par
num = int(input('Digite um numero: '))

x = 0
while x <= num:
    print('Este numero é par: ', x)
    x += 2
total = len(str(x))
print('Quantidade de digitos: ',total)