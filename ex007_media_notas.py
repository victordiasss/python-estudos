# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre
# a sua média.
nota1 = float(input('Digite o valor da primeira nota:'))
nota2 = float(input('Digite o valor da segunda nota:'))
total = nota1 + nota2
media = total / 2

print('O valor total das notas é: {} e a média das notas é: {}'.format (total, media))
