print('\t******** EMPRESA TCHAU - TELEFONIA *******')
gastos_mi = int(input('Gasto em minutos: '))
fatura = 0
if gastos_mi <= 0:
    print('Este mês você não precisa pagar a fatura está {:.2f} reais.'.format(fatura))
elif gastos_mi < 200:
    print('Você gastou abaixo de 200 minutos, então será 0.20 por minutos')
    fatura = gastos_mi * 0.20
#    print('Sua Fatura de telefonia será: {:.2f} reais.'.format(fatura))
elif gastos_mi >= 200 and gastos_mi <= 400:
    print('Você gastou acima de 200 e abaixo 400 minutos, então será 0.18 por minutos')
    fatura = gastos_mi * 0.18
#    print('Sua Fatura de telefonia será: {:.2f} reais.'.format(fatura))
else:
    print('Você gastou acima de 400 minutos, então será 0.15 por minutos')
    fatura = gastos_mi * 0.15
print('Sua Fatura de telefonia será: {:.2f} reais.'.format(fatura))