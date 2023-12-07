# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
cont= 0
cont2=0
atual= date.today().year
for c in range(1, 7+1):
    pessoa = int (input(f' Em que ano a {c}º pessoa nasceu ? '))
    idade= atual - pessoa
    if idade >= 21: 
        cont += 1
        
    elif idade < 21:
        cont2 += 1

print (f'Ao todo tivemos {cont} pessoas maiores de idade')
print (f'E também tivemos {cont2} pessoas menores de idade')
