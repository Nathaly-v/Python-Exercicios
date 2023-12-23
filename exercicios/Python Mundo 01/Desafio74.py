# Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
maiorNumero=0
menorNumero=0

cont = 0
print(' Os valores sorteados foram: ', end=' ')
while cont != 5:
    numeros = (randint(1, 10))
    cont +=1
    print (f'{numeros}',end= ' ')
    if cont == 1:
        maiorNumero = numeros
        menorNumero = numeros
    elif numeros > maiorNumero:
        maiorNumero = numeros
    elif numeros < menorNumero:
        menorNumero = numeros    
        
print(f'\n O maior valor sorteado foi: {maiorNumero}')
print(f' O maior valor sorteado foi: {menorNumero}')