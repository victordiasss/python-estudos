# Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.

nome = input("Digite seu nome completo: ")
nome_split = nome.split()

print("Primeiro nome: ", nome_split[0])
print("Último nome: ", nome_split[-1])
