# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = input ('Digite uma frase : ').replace(' ', '').upper()
frase1 = frase [::-1]
print (f'O inverso de {frase} é {frase1}')   

if frase == frase1:
    print('Temos um palíndromo !')
else:
    print('A frase digitada NÃO é um palíndromo !')