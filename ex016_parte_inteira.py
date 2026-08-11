# Crie um programa que leia o número Real qualquer e mostre na tela a sua porção
# inteira.

import math

n = float(input('Digite um número que possa ser arredondado:'))

print('A porção inteira do número digitado é: {}'.format(math.floor(n)))
