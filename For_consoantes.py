lista ='Ricardo'
vogal = 0
cons = 0
num = 0

for i in lista:
    if i in 'aeiou':
        vogal += 1
    elif i not in 'aeiou':
        cons += 1
    elif i in '0123456789':
        num += 1
print('Quantidade de vogais e consoantes')
print('Vogais      : ',vogal)
print('Consoantes  : ',cons)
#print('Números     : ',num)
print('Total letras: ', vogal + cons + num)
