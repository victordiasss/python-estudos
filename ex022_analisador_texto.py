# Crie um programa que leia o nome completo de uma pessoa
# e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

nome = input("Digite seu nome completo: ")
print("Nome em maiúsculas: ", nome.upper())
print("Nome em minúsculas: ", nome.lower())
print("Quantidade de letras (sem espaços): ", len(nome.replace(" ", "")))
print("Quantidade de letras no primeiro nome: ", len(nome.split()[0]))
