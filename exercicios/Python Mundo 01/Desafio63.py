# Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:

#0 – 1 – 1 – 2 – 3 – 5 – 8
print('-'*50)
print('Sequência de Fibonacci')
print('-'*50)
cont = 0 
n1 = 0
n2= 1
n3 = 0

# 0+1 = 2 / 1+2 = 3/ 2+3 = 5 / 3+5 = 8 / 5+8 = 13
termo= int(input(' Quantos termos você quer mostra? '))

while cont < termo:
    print(f'{n1}',end = ' > ')
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    cont += 1
print('FIM')            
    

        
        
        