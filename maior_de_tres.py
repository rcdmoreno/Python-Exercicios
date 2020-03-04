'''
Comentário de varias linhas com três aspas
Faça um Programa que leia três números e mostre o maior deles
'''
a = int(input('Primeiro: '))
b = int(input(' Segundo: '))
c = int(input('Terceiro: '))

if a > b and a > c:
    print('Primeiro é {} número é maior'.format(a))
elif b > a and b > c:
    print('Segundo é {} número é maior'.format(b))
elif c > a and c > b:
    print('Terceiro é {} número é maior'.format(c))
else:
    print('Os números são iguais.')
