# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

saida = 'S' 
lista=list()

while saida == 'S':
    valor=int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print(' Valor adicionado com sucesso...')
    else:
        print(' Valor duplicado, NÃO vou adicionar...')    
    saida=input('Quer continuar? [ S/N ]').upper()    
lista.sort()
print('=-'*50)  
print(f'Você digitou os valores: {lista}')  