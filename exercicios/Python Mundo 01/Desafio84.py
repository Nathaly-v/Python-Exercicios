# Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,                                      guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.                                                                                                              B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves. 

pessoas = list()
pessoasTudo= list()
contPessoas= 0
maiorPeso= 0
menorPeso= 0
nomeMaiorPeso = ''
nomeMenorPeso = ''
print(' ----------+ CADASTRO +----------')
while True:
    pessoas.append(input(' Nome: '))
    pessoas.append(int(input(' Peso: ')))
    contPessoas += 1
    pessoasTudo.append(pessoas[:])
    pessoas.clear()
    saida = input(' Deseja continuar? [ S/N ]: ').upper()
    if saida == 'N':
        break
for p in pessoasTudo:
    if contPessoas == 1:
        maiorPeso = p[1]
        menorPeso = p[1]
        nomeMaiorPeso = p[0]
        nomeMenorPeso = p[0]
    else:
        if p[1] > maiorPeso:
            maiorPeso = p[1]
            nomeMaiorPeso = p[0]
        elif p[1] < menorPeso:
            menorPeso = p[1]
            nomeMenorPeso = p[0]


print(f' Ao todo, você cadastrou {contPessoas} pessoas.')   
print(f' O maior peso foi de {maiorPeso}.0Kg. Peso de {nomeMaiorPeso} ')
print(f' O menor peso foi de {menorPeso}.0Kg. Peso de {nomeMenorPeso} ')