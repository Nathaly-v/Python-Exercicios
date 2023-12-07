# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for pessoa in range (1, 5 + 1):
    peso= float(input('Digite um peso'))
    if pessoa == 1:
        maiorPeso=peso
        menorPeso=peso
    elif peso > maiorPeso:
        
        maiorPeso= peso 
    
    elif peso < menorPeso:
        
        menorPeso= peso
    
print (f'maior {maiorPeso}')

print (f' menor {menorPeso}')