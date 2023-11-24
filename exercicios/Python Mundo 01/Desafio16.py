# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

n1=float(input('Digite um número : '))

int= math.trunc(n1)

print (f'o número {n1} tem a parte inteira de {int}. ')