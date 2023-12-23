# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
par = 0
cont = 0
cont9 = 0

op1=int(input(' Digite um número: '))
op2=int(input(' Digite outro número: '))
op3=int(input(' Digite mais um número: '))
op4=int(input(' Digite o último número: '))
    
numeros = (op1, op2, op3, op4)

posicao = numeros.index(3)


print(f'Você digitou os valores {numeros}')
print(f' O valor 9 apareceu {cont9} vezes.')
print(f' O valor 3 apareceu na {posicao +1} posição.')
print(f' Os valores pares digitados foram {par}')