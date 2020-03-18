'''
    Algoritmo de euclides do MDC exemplo: mdc(21,15) = 3
'''
a = int(input('A: '))
b = int(input('B: '))

while a % b != 0:
    a, b = b, a % b
print('MDC é {}'.format(b))