'''
Faça um pograma para loja de tintas. o Pograma devcerá pedir
o tamanho em metros quadrados da área a ser pintada. Considere que
a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que
tinta vendida em latas de 18 litros, que custam R$ 80,00.
Informa ao usuario a quantidade de latas de tintas a serem compradas e
preço total.
Obs: somente serão vendidos numeros inteiro de latas
'''
import time
lata = 18
preco_lata = 80
rendimento = 3
qtd_latas = 0
nome = input('Digite seu nome: ')
area = int(input('Digite a área ser pintada: '))
cobertura = (lata * rendimento)
if area % cobertura != 0:
    qtd_latas = int(area / cobertura) + 1
else:
    qtd_latas = int(area/ cobertura)
preco_total = (qtd_latas * preco_lata)
print('Sr(a). {} vai precisar de {} lata(s) para área de {} m²'.format(nome, qtd_latas, area))
print('O valor total da Nota Fiscal será: {}'.format(preco_total))
print('>>>>>>>>>>> imprimindo >>>>>>>>>>>>')
time.sleep(5)
