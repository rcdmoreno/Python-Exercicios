import datetime
import os
data_atual = datetime.date.today().strftime("%m/%d/%Y")
print('Data atual: ', data_atual)
idade = int(input('Digite Ano de fabricação do seu carro: '))
data_carro = str(datetime.date.today())
ano = int(str(data_carro)[:4])
while (idade > ano):
    os.system('clear')
    idade = int(input('Ano de fabricação deve ser menor ou igual Ano atual! {}\nDgite novamente: '.format(ano)))
if (ano - idade) > 10:
    print('Seu carro é velho e não contribui com IPVA anual, pois ele tem {} anos.'.format(ano - idade))                
if (ano - idade) <= 10:
    print('Seu carro é novo e deve contribuir com IPVA anual, pois ele tem somente {} anos.'.format(ano - idade))         

