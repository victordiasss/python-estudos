# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite os KM percorridos:'))
dias = int(input('Digite quantos dias o carro foi alugado:'))
precokm = km * 0.15
precodia = dias *60

valor = precokm + precodia

print("O valor a pagar pelo aluguel do carro é de R${:.2f}".format(valor))
