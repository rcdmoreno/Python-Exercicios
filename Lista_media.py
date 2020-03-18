import os
notas = []
soma = 0
cont = 1

print('Escola Estadual SP')
qtd = int(input('Informe qtd de notas: '))

while cont <= qtd:
    os.system('clear')
    print('Escola Estadual SP')
    print('Informe da Nota:{}'.format(cont))
    num = float(input('Nota: '))
    notas.append(num)
    soma += num
    cont+=1

print('Notas lançadas:', notas)
print('Média das notas é: {:.2f}'.format(soma/qtd))
