# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros
# e milímetros.

metros = float(input('Digite um valor em metros desejado:'))

km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print('O valor em km é {}, o valor em hm é {},\n o valor em dam é {}, o valor em cm é {}, o valor em mm é {}'.format(km, hm, dam, dm, cm,mm))
