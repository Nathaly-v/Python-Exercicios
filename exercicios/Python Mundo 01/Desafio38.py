# Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

# – O primeiro valor é maior

# – O segundo valor é maior

# – Não existe valor maior, os dois são iguais

n1= int(input(' - Primeiro número : '))
n2= int(input(' - Segundo número : '))

if n1 > n2 :

    maior = n1
    
    print (f' O primeiro valor é maior ')
    
elif n2 > n1 :

    maior = n2
        
    print (f' o segundo valor é maior')
        
else :
    print (' os dois valores são iguais ')