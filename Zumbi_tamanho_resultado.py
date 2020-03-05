linha = '- -'
coluna = '|'
print(linha * 500)
print(coluna * 1)
print('\t Calcular o quantos Digitos tem um número elevado ao outro\n')
print(coluna * 500)
print(coluna * 1)
print('\t O valor elevado deve ser menor do que 100\n')

print(coluna * 1)

num = float(input('Digite o número desejado: '))

elev = float(input('O número será elevado: '))
while (elev > 100):
    elev = float(input('O valor muito alto, digite novamente: '))
valor = num ** elev
print('O número %f'%num, 'elevado %f'%elev, 'ao será: %f' %valor)
print('A quantidade de caracters é :',len(str(valor)))
