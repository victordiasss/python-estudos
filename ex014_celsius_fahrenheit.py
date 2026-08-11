# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

celsius = float(input('Digite o valor em graus celsius: ºC'))
fahrenheit = celsius * 9 / 5 + 32

print(f'A temperatura de ºC{celsius}, corresponde a ºF{fahrenheit}')
