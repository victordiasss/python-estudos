# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um
# dos dígitos separados.

numero = int(input("Digite um número de 0 a 9999: "))
numero = str(numero)
numero = numero.zfill(4)

print(numero[0])
print(numero[1])
print(numero[2])
print(numero[3])
