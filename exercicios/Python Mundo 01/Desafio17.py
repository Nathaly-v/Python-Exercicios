# Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot

oposto = float (input('Comprimento do Cateto Oposto : '))
adjascente= float (input ('Comprimeto do Cateto Adjascente'))

triangulo= hypot (oposto , adjascente)

print (f'A hipotenusa vai medir :{triangulo :.2f}.')
