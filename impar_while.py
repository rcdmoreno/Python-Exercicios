print('P = PAR\nI = IMPAR ' )
print('Vamor verificar valores par e impar até valor digitado.')
num = int(input('Digite um número: '))

x = 0
p, i = 0, 0
while x < num:
    if x % 2 == 0:
       print('P: ', x)
        p+=1
    else:
       print('I: ', x)
        i+=1
    x += 1
print('Qtd. valores Pares: ',p)
print('Qtd. Valores Impar: ',i)