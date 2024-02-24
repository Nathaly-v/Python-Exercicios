# Crie um programa que peça ao usuário o nome de um produto, em seguida crie um identificador 
# único atrelado ao mesmo.
#Regras
#[ ! ] - Cada identificador precisa começar com 2 letras e terminar com 4 números;
#[ ! ] - Armazene todos os identificadores em um único arquivo no excel;
#[ ! ] - Não pode haver mais de um identificador único igual a outro;

#Extra: Crie uma opção de consultar os identificadores e produtos armazenados

import pandas as pd
import random
import string



listaCodigos = list()
def gerarCodigoAleatorio():   
    letras = string.ascii_uppercase
    duasLetras =''.join(random.choices(letras, k=2))
    quatroNumeros=''.join(random.choices(string.digits, k=4))
    combinacaoAleatoria=duasLetras + quatroNumeros

    while combinacaoAleatoria in listaCodigos:
        duasLetras =''.join(random.choices(letras, k=2))
        quatroNumeros=''.join(random.choices(string.digits, k=4))
        combinacaoAleatoria=duasLetras + quatroNumeros    
    listaCodigos.append(combinacaoAleatoria)
    return combinacaoAleatoria

while True:
    print('=+'*30)
    print('\n \t ------+ MENU +------ ')
    print (''' 
    \t [ 1 ] Adicione Produtos
    \t [ 2 ] Consultar os Dados existentes
    \t [ 3 ] Sair\n''')
    print('=+'*30)
    menu = int(input(' Digite a opcao desejada:'))
   
    if menu == 1:
        listaDosProdutos = list()
        try:
            df = pd.read_excel('produtos.xlsx') 
            listaDosProdutos = df.to_dict(orient='records') 
        except FileNotFoundError:
            pass
        while True:    
            opcao = input('Digite o nome do produto desejado: ').upper()
            listaDosProdutos.append({'Produto': opcao , 'Código': gerarCodigoAleatorio()})
            saida = input(' Deseja adicionar outro produto? [ S/N ] ').upper()
            df = pd.DataFrame(listaDosProdutos)
            nomeArquivo = 'produtos.xlsx'
            df.to_excel(nomeArquivo, index = False)

            if saida == 'N':
                break
            else:
                pass
        print(f'Os produtos foram salvos no arquivo {nomeArquivo} com sucesso.')
    elif menu == 2:
        try:
            df = pd.read_excel('produtos.xlsx')
            print('\t =+=+=+=+=+=+=+ PRODUTOS CADASTRADOS!  =+=+=+=+=+=+=+')
            for produto, id in zip(df['Produto'], df['Código']):
                    print(f'Produtos: {produto} - Códigos: {id}')
                    
        except FileNotFoundError:
            print("Nenhum arquivo encontrado.")

    elif menu == 3:   
        print(' FINALIZADO !')
        break

