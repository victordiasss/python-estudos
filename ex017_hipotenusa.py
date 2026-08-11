# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

cateto_oposto = float(input('Digite o número do cateto oposto: '))
cateto_adjacente = float(input('Digite o número do cateto adjacente: '))
cat_opo_adj_quadrado = (cateto_oposto ** 2) + (cateto_adjacente ** 2)
hipotenusa = math.sqrt(cat_opo_adj_quadrado)

print('O resultado da hipotenusa é: {:.2f}'.format(hipotenusa))
