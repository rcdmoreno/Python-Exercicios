# soma 15 numero inteiro
import os
n = 1
soma = 0
qtd = 3
while n <= qtd:
    os.system('clear')
    print('\t\t\t\t\t\t\tSoma de 15 números Inteiro.\n')
    print('\tsomatório esta em: ',soma)
    print('\tCiclos: {} \ {}'.format(qtd,n))
    x = int(input('\tDigite um número: '))
    n += 1
    soma = soma + x
print('\tTotal da soma 10 primeiros numero é:', soma)
