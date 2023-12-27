#  Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = list()
for _ in range (0, 5):
    valor = int (input(f'Digite um valor para a Posição {_}: '))
    lista.append(valor)  
    
maiorNumero=max(lista)
menorNumero=min(lista)


print('=-'*50)
print(f'Você digitou os valores: {lista}') 
print(f'O maior valor digitado foi {maiorNumero} nas posições:', end=' ')

for i in range(0, len(lista)):
    if lista[i] == maiorNumero:
        print(f'{i}', end = '...')

    
print(f'\n O menor valor digitado foi {menorNumero} nas posições: ', end =' ')
for e in range (0, len(lista)):
    if lista[e] == menorNumero:
        print(f'{e}', end ='...')