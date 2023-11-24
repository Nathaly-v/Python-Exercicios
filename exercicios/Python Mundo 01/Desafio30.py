# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num= int (input (' - Me diga um número qualquer ! '))

resto = num%2

if resto == 0:
    print (f' par')
    
else : 
    print('número é impar')
    
