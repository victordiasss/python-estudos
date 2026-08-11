# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
# quantos Dólares ela pode comprar. Considerar US$1,00=R$3,27

dinheiro = float(input('Digite o valor que tem na carteira: R$'))
compra_dolar = dinheiro / 5.13

print("Com R${} você pode comprar US${:.2f} dólares.".format(dinheiro, compra_dolar))
