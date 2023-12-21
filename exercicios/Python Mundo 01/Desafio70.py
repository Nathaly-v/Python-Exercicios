# Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

print('-'*50)
print(' LOJA SUPER BARATÃO ')
print('-'*50)
saida = 'S'
somaValores = 0
contPreco = 0
menorPreco = 0
contProduto = 0
nomeProduto = 0
while saida == 'S':
    produto= input(' Nome do Produto: ').strip()
    preco= float(input(' Preço: ').strip())
    
    somaValores = somaValores + preco
    if preco > 1000.00:
       contPreco +=1 
       
    if contProduto == 0:
        menorPreco = preco   
    elif preco < menorPreco:
        menorPreco = preco 
        
    if contProduto == 0:
        menorPreco = preco
        nomeProduto = produto
    elif preco < menorPreco:
        menorPreco=preco 
        nomeProduto=produto
    contProduto +=1    
    saida = input(' Quer continuar? [S / N]').strip().upper()[0]
print('-'*20 + f'FIM DO PROGRAMA' + '-'*20)
print(f' O total de compra foi R$ {somaValores}.')
print(f' Temos {contPreco} produtos custando mais de R$ 1000.00 ')
print(f' O produto mais barato foi {nomeProduto} que custa {menorPreco}')
    