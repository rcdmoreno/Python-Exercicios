import os
numeros = []
numeros_inversa = []
cont = 1
print('Carrega uma lista x números e imprimir na ordem normal e inversa\n')
qtd = int(input('Informe qtd de números: '))

# imprimindo o lista normal
while cont <= qtd:
    os.system('clear')
    print('Informe o número: {}'.format(cont))
    num = int(input('Valor: '))
    numeros.append(num)
    cont+=1
print('Lista de contêm {} números com seus valores na ordem normal : {}'.format(qtd,numeros))

# imprimindo o lista inversa
cont = qtd - 1
while cont >= 0:
    numeros_inversa.append(numeros[cont])
    cont -= 1
print('Lista de contêm {} números com seus valores na ordem inversa: {}'.format(qtd, numeros_inversa))
print('\n')