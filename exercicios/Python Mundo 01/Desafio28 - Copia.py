# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import emoji
from random import randint
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

print ('-=-' *20)
print(yellow + 'Vou pensar em um número entre 0 e 5. TENTE ADIVINHAR '+ normal)
print ('-=-' *20)

n1=int(input(purple + ' - Em que número eu pensei ?  '+ normal))

computador= randint(0,5)

print (('.'*10) + yellow + 'PROCESSANDO' + normal + ( '.'*10))
sleep(2)
if n1 == computador:
     print(purple + f' - PARABÉNS !! Você conseguiu me vencer'+ normal +  emoji.emojize(':confetti_ball:'))
    
else:
    print(yellow + f' - Ganhei, EU pensei {computador} e não em : {n1}' +normal + emoji.emojize(':OK_hand:'))

