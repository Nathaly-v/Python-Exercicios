# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.                                                                                                              B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves. 

pessoas = list()
pessoasTudo= list()
contPessoas= 0
maiorPeso= float('-inf')
menorPeso= float('inf')

nomeMaiorPeso = list()
nomeMenorPeso = list()

print(' ----------+ CADASTRO +----------')
while True:
    
    nome=input(' Nome: ')
    peso=int(input(' Peso: '))
    
    pessoas.append(nome)
    pessoas.append(peso)      
    pessoasTudo.append(pessoas[:])
    pessoas.clear()
    contPessoas += 1

    if peso > maiorPeso:
        maiorPeso = peso
        nomeMaiorPeso=[nome]
    elif peso == maiorPeso:
        nomeMaiorPeso.append(nome)
    if peso < menorPeso:
        menorPeso= peso
        nomeMenorPeso=[nome]
    elif peso == menorPeso:
        nomeMenorPeso.append(nome)

    saida = input(' Deseja continuar? [ S/N ]: ').upper()
    if saida == 'N':
        break

print(f' Ao todo, você cadastrou {contPessoas} pessoas.')   
print(f' O maior peso foi de {maiorPeso}.0Kg. Peso de {nomeMaiorPeso} ')
print(f' O menor peso foi de {menorPeso}.0Kg. Peso de {nomeMenorPeso} ')