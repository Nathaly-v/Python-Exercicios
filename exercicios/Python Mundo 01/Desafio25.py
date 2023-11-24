# Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome= input(' Qual é o seu nome completo ? ').upper()

frase= 'SILVA' in nome

print(f'Seu nome tem Silva ? {frase}. ')
