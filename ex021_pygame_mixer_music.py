# Faça um programa em Python que abra e reproduza o áudio de um arquivo
# MP3. Considerar que o arquivo .mp3 está na mesma pasta do arquivo .py

import pygame

pygame.mixer.init()
pygame.mixer.music.load('anjos.mp3')
pygame.mixer.music.play()

input("Pressione Enter para parar a música.")
