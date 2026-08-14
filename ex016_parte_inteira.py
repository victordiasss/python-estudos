# Crie um programa que leia o número Real qualquer e mostre na tela a sua porção
# inteira.

import math

n = float(input('Digite um número: '))

print('A porção inteira do número {} é: {}'.format(n, math.trunc(n)))
