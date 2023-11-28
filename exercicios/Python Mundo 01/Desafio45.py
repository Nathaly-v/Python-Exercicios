# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep 

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
normal = "\033[0m" # to come back to default

print (yellow + ('+=+' *15) + ' JOKENPÔ ' + ('+=+' * 15) + normal )
cont=0
while True :
    print (purple + ' Suas opções : ')
    print (' [ 1 ] PEDRA ')
    print (' [ 2 ] PAPEL ')
    print (' [ 3 ] TESOURA '+ normal)

    player = int (input (yellow + '\n Qual é a sua Jogada ? ' + normal))

    player2= random.choice([ 'Pedra', 'Papel', 'Tesoura' ])

    print ( purple +' \n JO ')
    sleep (1)
    print (' KEN ')
    sleep (1)
    print (' PÔ !!! \n'+ normal)
    sleep (1)


    if  player == 1:
        player1 = 'Pedra'
        print (yellow +'=' * 50)
        print ( f' Computador jogou {player2} ')
        print (f' Você jogou {player1} ' )
        print ('=' * 50 + normal) 

        if player2 == 'Papel':
            print (blue +'\n Computador VENCE ! \n'+ normal)
            
        elif player2 == 'Tesoura':
            print (purple + '\n Você VENCE !\n'+ normal)
            
        elif player2 == 'Pedra': 
            print (green + '\nEMPATE !\n' + normal)
            
    if player == 2:
        player1 = 'Papel'
        print (yellow +'=' * 50)
        print ( f' Computador jogou {player2} ')
        print (f' Você jogou {player1} ' )
        print ('=' * 50 + normal) 
        
        if player2 == 'Pedra':
            print (purple + '\n Você VENCE ! \n' + normal)
            
        elif player2 == 'Tesoura' :
            print (blue + '\n Computador VENCE !\n' + normal)
            
        elif player2 == 'Papel': 
            print (green + '\nEMPATE !\n' + normal)
        
    if  player == 3:
        player1 = 'Tesoura'
        print (yellow +'=' * 50)
        print ( f' Computador jogou {player2} ')
        print (f' Você jogou {player1} ' )
        print ('=' * 50 + normal) 
        
        if player2 == 'Papel' :
            print ( purple + '\n Você VENCE ! \n' + normal)
            
        elif player2 == 'Pedra' :
            print (blue +' \nComputador VENCE! \n'+ normal)
            
        elif player2 == 'Tesoura' : 
            print (green + '\nEMPATE !\n' + normal) 
    elif player > 3:
        print (red +' OPÇÃO INVÁLIDA ! Tente novamente ... ' + normal)    
    if cont == 10 :           
        op= input (green + '\n Digite [S] para SIM OU [N] para NÃO: \n'+ normal).upper() 
        if op == 'N':
            break
    cont += 1
  
 
# pedra > tesoura
# papel > pedra
# tesoura > papel



 


    