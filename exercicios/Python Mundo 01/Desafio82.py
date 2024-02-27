# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

listaCompleta = list()
listaImpar = list()
listaPar = list()
while True:
    opcao = int(input('Digite um número: '))
    listaCompleta.append(opcao)
    if opcao % 2 == 0:
        listaPar.append(opcao)
    elif opcao % 2 != 0:
        listaImpar.append(opcao)
    saida = input(' Deseja continuar ? [ S/N ]').upper()
    if saida == 'N':
        break
    else:
        pass
listaPar.sort()
listaImpar.sort()
print(f' A lista completa é : {listaCompleta}')
print(f' A lista de pares é : {listaPar}')
print(f' A lista de ímpares é: {listaImpar}')