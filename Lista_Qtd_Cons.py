'''
Ao preencer umas lista o programa deve contar quantas são caracteres é consoantes;

'''
letras = []
i = 1
n_letras = int(input('Qual tamanho da lista: '))

while i <= n_letras:
    print('Letra:',i)
    letras.append(input("Informe a Letra: "))
    i += 1
i = 0
cons = 0
vogal = 0
while i <= (n_letras - 1):
    if letras[i] not in 'aeiou':
        cons += 1
    elif letras[i] in 'aeiou':
        vogal += 1    
    i += 1
print(letras)
print("Total de Vogais: ", vogal)
print("Total de Consoantes: ", cons)
print('Total de Caracters: ',vogal + cons)