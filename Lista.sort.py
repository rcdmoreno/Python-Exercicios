import os
numeros = []
cont = 1
print('Carrega uma lista de valores X e imprimir na ordem normal de lançamento.\nEm seguida Imprimir ordem descrente e descrecente')
qtd = int(input('Informe qtd de números: '))

# imprimindo o lista normal
while cont <= qtd:
    os.system('clear')
    print('Total de loopping {}/{}:'.format(qtd,cont))
    num = int(input('Valor: '))
    numeros.append(num)
    cont+=1
print('Lista de contêm {} números na ordem lançamento   : {}'.format(qtd,numeros))
print('Lista de contêm {} números na ordem crescente    : {}'.format(qtd,sorted(numeros)))
print('Lista de contêm {} números na ordem descrescente : {}'.format(qtd,sorted(numeros,reverse=True)))


