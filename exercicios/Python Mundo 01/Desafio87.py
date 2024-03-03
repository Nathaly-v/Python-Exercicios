# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:  
#A) A soma de todos os valores pares digitados.                                                                                                 
#B) A soma dos valores da terceira coluna. 
#C) O maior valor da segunda linha.
pares = list()
terceiraColuna = list()
matriz= [[0,0,0],[0,0,0],[0,0,0]]
maiorNumeroSegundaLinha = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f' Digite um valor para: [{l}], [{c}]: '))
        if matriz [l][c] % 2 == 0:
            pares.append(matriz[l][c])
        if c == 2:
            terceiraColuna.append(matriz [l][c])
        if l == 1 and matriz [l][c] > maiorNumeroSegundaLinha:
            maiorNumeroSegundaLinha = matriz[l][c]   
print('=-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz [l][c] :^5}]', end = '')
    print()
print('=-'*30)
somaPares=sum(pares)
print(f' A soma dos valores pares é {somaPares}.')
somaTerceiraColuna = sum(terceiraColuna)
print(f' A soma dos valores da terceira coluna é {somaTerceiraColuna}.')
print(f' O maior valor da segunda linha é {maiorNumeroSegundaLinha}.')