# Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e 
# preencha com valores lidos pelo teclado. 
# No final, mostre a matriz na tela, com a formatação correta.
ordem = [ [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2] ]
novaOrdem=list()
for c in range (0, 9):
    valor=int(input(f' Digite um valor para {(ordem[c])}: '))
    novaOrdem.append(valor)
    
print('=-'*30)
print(f'[{(novaOrdem[0]):^5}]  [{(novaOrdem[1]):^5}]  [{(novaOrdem[2]):^5}]')
print(f'[{(novaOrdem[3]):^5}]  [{(novaOrdem[4]):^5}]  [{(novaOrdem[5]):^5}]')
print(f'[{(novaOrdem[6]):^5}]  [{(novaOrdem[7]):^5}]  [{(novaOrdem[8]):^5}]')