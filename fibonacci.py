n = int(input('Digite um número: '))
a, b = 1, 1
k = 1

while k <= n - 2:
    a, b = b, a + b
    k = k + 1
print('Fibonacci({}) = {}'.format(n,b))