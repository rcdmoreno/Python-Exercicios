condutor = input('Digite nome do condutor: ')
veloc = float(input('Velocidade registrada no RadarSpot: '))
multa = 0
if veloc > 110:
    print('Sr. {}, o limite da via é 110 km/h, e foi registrada um velocidade de {}\n,sendo acima do limtite. Neste caso Sr. será multado R$ 5,00 por km acima de 110'.format(condutor, veloc))
    multa = (veloc - 110) * 5.00
    print('O valor da Multa é: {:.2f}'.format(multa))
if veloc <= 110:
    print('Sr. {} você dirigiu no limite da via 110 km/h, sua velocidade registrada foi de {} km/h.\nParabêns por dirigir com segurança.'.format(condutor, veloc))
    print('O valor da Multa é: {:.2f}'.format(multa))
