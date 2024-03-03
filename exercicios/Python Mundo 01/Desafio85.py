# Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores 
# numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. 
#No final, mostre os valores pares e ímpares em ordem crescente.
numeros = [[], []]


for c in range (1, 8):
    valor= int(input(f' Digite o {c}° valor: '))
    if valor % 2 == 0:
       numeros[0].append(valor)
    elif valor % 2 != 0:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()      
print(f'=-'*25)
print(f' Os valores pares digitados foram:{numeros[0]}')
print(f' Os valores ímpares digitados foram: {numeros[1]}')
