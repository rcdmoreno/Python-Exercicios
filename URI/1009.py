vendedor = input("")
salario = input("")
total_vendas = input("")
salario = float(salario) + (float(total_vendas) * 0.15)
print("TOTAL = R$ {:.2f}".format(salario))