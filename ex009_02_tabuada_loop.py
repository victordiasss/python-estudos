# Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada.

numero = int(input('Digite um número inteiro:'))

for tabuada in range(1, 10):
    resultado = numero * tabuada
    print(f'{numero} * {tabuada} = {resultado}')
