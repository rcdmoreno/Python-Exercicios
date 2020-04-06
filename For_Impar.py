
def encontrar_impar_for(start, end, list):
    while start <= fim:
        lista.append(int(input('N: ')))
        start += 1
    print('O valores da Lista: ', lista) 

    for i in lista:
        if i % 2 != 0:
            print('O valores da Lista impar: ', i) 

lista = []
print("Lista de Numeros e quais são os Impares?")
inicio = int(input('Qual inicio do For: '))
fim = int(input('Qual é fim do For: '))

encontrar_impar_for(inicio, fim, lista)