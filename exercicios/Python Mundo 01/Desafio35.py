# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float (input (' - Primeiro Segmento : '))
b = float (input (' - Segundo Segmento : '))
c = float (input (' - Terceiro Segmento : '))

if (a + b) > c :
    if (b + c) > a :
        if (a + c) > b :
            print (f'Os segmetos acima , formam um triangulo ')
        else:
            print (f'Os segmetos acima , NÃO formam um triangulo ')
else: 
    print (f'Os segmetos acima , NÃO formam um triangulo : ')