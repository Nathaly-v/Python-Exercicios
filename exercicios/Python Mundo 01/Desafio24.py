# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade= input('Em que cidade você nasceu ? ').upper()

frase= (cidade.split()[0])in('SANTO')

print(f'{frase}')