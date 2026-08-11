# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo:')

print(type(n))
print('É númerico?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Está em maísculas?', n.isupper())
print('Está em minúsculas?', n.islower())
print('Está capitalizada? (A primeira letra é maiúscula e a demais são minúsculas.', n.istitle())
print('Tem apenas espaços?', n.isspace())
