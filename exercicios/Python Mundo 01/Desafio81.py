#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.                   
#Depois disso, mostre:             
 #   A) Quantos números foram digitados.                                                  
 #   B) A lista de valores, ordenada de forma decrescente.                                                                                          
 #   C) Se o valor 5 foi digitado e está ou não na lista.

numeros = list()
temCinco = False
cont = 0

while True:
    valor = int(input(' Digite um valor: '))
    numeros.append(valor)
    cont += 1
    saida = input(' Quer continuar? [ S/N ]').upper()
    if saida == 'N':
        break
    elif saida == 'S':
        pass
    else:
        break
listaDecrescente = numeros
listaDecrescente.sort(reverse=True)
try:
    if numeros.index(5) == True :
        temCinco = True
except:
    pass
    
print('=-'*50)
print(f' Você digitou {cont} elementos.')
print(f' Os valores em ordem decrescente são : {listaDecrescente}')
if temCinco == True:
    print('O valor 5 faz parte da lista! ')
else:
    print('O valor 5 não foi encontrado na lista!')