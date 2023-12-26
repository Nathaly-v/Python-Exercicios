# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

cont3 = 0
text = ""

while True:
    op1=int(input(' Digite um número: '))
    op2=int(input(' Digite outro número: '))
    op3=int(input(' Digite mais um número: '))
    op4=int(input(' Digite o último número: '))
    break

numeros = (op1, op2, op3, op4)
if 3 in numeros:
    cont3 = numeros.index(3) + 1
    text = f' O valor 3 apareceu na {cont3}ª posição'
else:
    text = f' O valor 3 não apareceu em nenhuma posição'

print(f'Você digitou os valores {numeros}')
print(f' O valor 9 apareceu {numeros.count(9)} vezes.')
print(f'{text}')
print(f' Os valores pares digitados foram: ', end = ' ')
for number in numeros:
    if number % 2 ==0:
        print(number, end = ' ')
    else:
        pass