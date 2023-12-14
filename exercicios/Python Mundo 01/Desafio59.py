# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

primeiroValor=int(input(' Primeiro Valor: ').strip())
segundoValor=int(input(' Segundo Valor: ').strip())


while True: 
    print('='* 10)
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR DO PROGRAMA')

    opcao=input(' >>>>>> Qual é a sua opção? ')

    if opcao == '1':
        somar= primeiroValor + segundoValor
        print(f'A soma entre {primeiroValor} e {segundoValor} é {somar}')

    elif opcao == '2':
        multiplicar= primeiroValor * segundoValor
        print(f'O resultado de {primeiroValor} e {segundoValor} é {multiplicar}')  
    elif opcao == '3':
        if primeiroValor > segundoValor:
            maior = primeiroValor
        elif segundoValor > primeiroValor:
            maior = segundoValor
        else:
            maior=primeiroValor
            print('Os valores são iguais')
        print(f'Entre {primeiroValor} e {segundoValor} o maior valor é {maior}')
    elif opcao == '4':
        print('Informe os números novamente')
        primeiroValor=int(input(' Primeiro Valor: ').strip())
        segundoValor=int(input(' Segundo Valor: ').strip())    
    if opcao == '5':
        print(' Finalizando... ')
        print('='*30)
        print('Fim do programa! Volte Sempre!')
    
        break
