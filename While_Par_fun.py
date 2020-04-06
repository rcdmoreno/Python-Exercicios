
def encontrar_impar(inicio, fim, lista):

    while inicio <= fim:
        lista.append(int(input('N: ')))
        inicio += 1
    print('o Valor da Lista é:',lista)

    i=0
    while i < fim:
        if lista[i] % 2 != 0:
            print('impar:',lista[i])
        i += 1

lista = []
inicio = int(input('Digite o primeiro: '))
fim = int(input('Digite o ultimo: '))

encontrar_impar(inicio, fim, lista)
