# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print (' 10 TERMOS DE UMA P.A.')

termo = int(input( 'Primeiro termo : '))
razao =  int(input( 'Razão : '))
cont = 0


for numero in range(termo ,999, razao) : 
    if cont == 10:
        break
    cont = cont +  1
  
    print(f'{numero} ', end= ' ↦ ')    

print( 'acabou' ) 

