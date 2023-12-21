# Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint 
print('=-'* 50)
print('VAMOS JOGAR PAR OU ÍMPAR: ')
print('=-'* 50)

cont = 0

while True: 
    op = int(input(' Digite um valor: ').strip())
    parImpar= input(' Par ou Ímpar ? [ P / I ]').strip().upper()
    
    pc = randint (0,10)
    soma = pc + op
    print('--'*50)
    print(f' Você jogou {op} e o computador {pc}. ', end = '')

    if soma % 2 == 0:
        print(f' Total de {soma} DEU PAR')
        print('--'*50)
        if parImpar == 'P':
            print(' Usuário VENCEU !')
            cont += 1
            print('Vamos jogar novamente...')
            print('=-'*50)
        else:
            print(' Usuário PERDEU !') 
            print(f' GAME OVER! Você venceu {cont} vezes.')                  
            break
    else: 
        print(f' Total de {soma} DEU ÍMPAR')
        print('--'*50)
        if parImpar == 'I':
            print(' Usuário VENCEU !')
            print('Vamos jogar novamente...')
            print('=-'*50)
            cont += 1
        else:
            print(' Usuário PERDEU! ') 
            print('=-'*50)
            print(f' GAME OVER! Você venceu {cont} vezes.')    
            break
    

    
   

    
    