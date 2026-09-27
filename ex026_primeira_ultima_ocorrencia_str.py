# Faça um programa que leia uma frase pelo teclado e mostre quantas
# vezes aparece a letra “A”, em que posição ela aparece a primeira
# vez e em que posição ela aparece a última vez.

frase = input("Digite uma frase: ")

print("A letra 'A' aparece", frase.upper().count("A"), "vezes.")
print("A primeira ocorrência da letra 'A' é na posição", frase.upper().find("A") + 1)
print("A última ocorrência da letra 'A' é na posição", frase.upper().rfind("A") + 1)
