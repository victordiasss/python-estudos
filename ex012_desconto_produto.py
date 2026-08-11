# Faça um algoritimo que leia o preço de um produto e mostre o seu novo preço, com 5%
# de desconto.

preco = float(input('Digite o preço do produto encontrado:'))
desconto = (preco / 100) * 95

print('O preço inicial do produto é: R${:.2f}. O preço final com 5% de desconto é de R${:.2f}'.format(preco, desconto))
