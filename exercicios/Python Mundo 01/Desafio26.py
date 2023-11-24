# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase=input('Digite uma Frase : ').upper()

a1= frase.count('A')
a2= frase.find('A')
a3= frase.rfind ('A')

print ('=' *50)

print (f' - A letra A , aparece : {a1} vezes na frase. ')
print (f' - A primeira letra A, apareceu na posição : {a2 +1}. ')
print (f' - A última letra A, apareceu na posição : {a3 +1}. ')

print ('=' *50)