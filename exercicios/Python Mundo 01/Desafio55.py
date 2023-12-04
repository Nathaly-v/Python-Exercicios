# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for c in range (1, 3):
    peso= float (input(f'Peso da {c}ª pessoa : '))  
    
    
for peso in range (1, 3):
    
    if peso[1] > peso[2]:
        maior = peso[1]
    elif peso[2] > peso[1]:
        maior = peso[2]
        
    if peso[1] > peso[2]:
        menor = peso[1]
    elif peso[2] > peso[1]:
        menor = peso[2]    
        
print (f'{maior}')
print (f'{menor}')
