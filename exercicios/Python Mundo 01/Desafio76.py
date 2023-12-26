# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
def centralizador(titulo, caractere=' ', largura_linha=40):
        espacos_laterais = (largura_linha - len(titulo) - 2) // 2
        linha = caractere * espacos_laterais + f' {titulo} ' + caractere * espacos_laterais
        return print(linha)
    
print('-'*50)
centralizador(' LISTAGEM DE PREÇOS ')
print('-'*50)

produtos = (
    ('Lápis', 1.75),
    ('Borracha', 2.00), 
    ('Caderno', 15.90), 
    ('Estojo', 25.00), 
    ('Transferidor', 4.20), 
    ('Compasso', 9.99), 
    ('Mochila', 120.32), 
    ('Canetas', 22.30), 
    ('Livro', 34.90) 
)

for item, valor in produtos:
    print('{:.<30}R$ {:.2f}'.format(item,valor))