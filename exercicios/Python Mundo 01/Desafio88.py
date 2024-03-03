# Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e 
# vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

import random

def GeradorDeNumerosAleatorios(limiteInferior, limiteSuperior):
    numerosDisponiveis = list(range(limiteInferior,limiteSuperior + 1))
    random.shuffle(numerosDisponiveis)
    while True:
        if not numerosDisponiveis:
            numerosDisponiveis = list(range( limiteInferior, limiteSuperior + 1)) 
            random.shuffle(numerosDisponiveis) 
                  
        yield numerosDisponiveis.pop()

limiteInferior = 1
limiteSuperior= 60
    
gerador = GeradorDeNumerosAleatorios(limiteInferior, limiteSuperior)

print('-'*50)
print(' \t\t JOGA NA MEGA SENA \t')
print('-'*50)

while True:
    opcao = int(input(' Quantos jogos você quer que eu sorteie? '))
    break
print('-=-=-= SORTEANDO 10 JOGOS -=-=-=')
for jogo in range (0, opcao):
    numeroJogo=list()
    for _ in range(6):
        numeroJogo.append(next(gerador))
    numeroJogo.sort()
    print(f'Jogo {jogo + 1} : ', end=' ')  
    print(f'{numeroJogo}', end='')
    print('') 
print('-=-=-=-=-=-=< BOA SORTE ! >-=-=-=-=-=-=')