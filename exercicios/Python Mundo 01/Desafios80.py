# Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e 
# cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). 
# No final, mostre a lista ordenada na tela.


numeros=list()

for cont in range (0,5):
    numero= int(input(' Digite um valor: '))
    
    while( numero in numeros):
        print(' Esse número já existe na lista! ')
        numero = int(input(' Digite outro valor: '))
        
    if cont == 0:
        numeros.append(numero)
        print(' O primeiro valor foi adicionado ao final da lista')
    else:
        if numero > max(numeros):
            numeros.append(numero)
            print(f' O valor foi inserido na posição {numeros.index(numero)}º')
        elif numero < min(numeros):
            print(f' O valor foi inserido na posição {numeros.index(numero)}º')    
        else:
            for i, num in enumerate(numeros):
                if numero <= num:
                    numeros.insert(i, numero)
                    print (f' O valor foi inserido na posição {i}º')
                    break

print('=-'*50) 
listaOrdenada = numeros [:]     
listaOrdenada.sort()

print(f' Valores ordenados usando função sort ({listaOrdenada})')
print(f' Valores ordenados usando o processo de lógica e análise {numeros}')                 