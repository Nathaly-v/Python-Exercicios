# Exercício Python 33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1= int (input('Digite um número: '))
n2= int (input('Digite um número: '))
n3= int (input('Digite um número: '))



if n1 >= n2 and n1 >= n3 : 

    maior = n1
    
elif n2 >= n1 and n2 >= n3 :    

    maior = n2
    
elif n3 >= n1 and n3 >= n2 :

    maior = n3
    
if n1 <= n2 and n1 <= n3:
    
    menor = n1
    
elif n2 <= n1 and n2 <= n3 :
    
    menor = n2
    
elif n3 <= n1 and n3 <= n2 :
    
    menor = n3
    
    
    
    
print (f' Maior número é : {maior}')

print (f' Menor número é : {menor} ')