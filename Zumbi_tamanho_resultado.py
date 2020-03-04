print('\t Calcular o quantos Digitos \n\t tem um número elevado ao outro\n')
num = int(input('Digite o número desejado: '))
elev = int(input('O número será elevado: '))
while (elev > 100):
    elev = int(input('O valor muito alto, digite novamente: '))
valor = num ** elev
print('O número %d'%num, 'elevado %d'%elev, 'ao será: %d' %valor)
print('A quantidade de caracters é :',len(str(valor)))
