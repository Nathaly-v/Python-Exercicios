# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador= randint (0, 10)
cont= 1
print('Acabei de pensar em um número entre 0 e 10.\n Será que você consegue adivinhar ?')

while True: 
    numero=int(input('Qual é seu palpite? ').strip())
    if numero < computador:
        print('MAIS ...  tente mais uma vez. ')    
    elif numero > computador: 
        print('Menos ... tente mais uma vez. ')
    elif numero == computador:
        break
    cont+=1
print(f' Acertou com {cont} Tentativas.Parabéns! ')     
    