# Exercício Python 083: Crie um prow# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e 
# fechados na ordem correta.

opcao = input(' Digite a expressão: ')

comeco = opcao.count('(')
fim = opcao.count(')')
soma = comeco + fim

if soma % 2 == 0:
    print(' Expressão CORRETA !')
else:
    print(' Expressão INCORRETA !')