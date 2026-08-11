# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário,
# com 15% de aumento.

salario = float(input('Digite o valor do seu salário:'))
aumento = salario * (15 / 100)
novo_salario = salario + aumento

print('Com aumento de 15%, o novo salário será: R${:.2f}'.format(novo_salario))
