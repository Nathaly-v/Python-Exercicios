# Faça um programa que mostre um menu com algumas opções, o usuário precisa escolher entre:
# @ Inserir informações novas (Sem apagar as existentes), 
# @ Ler as informações atuais (Mostrar no Terminal),
# @ Excluir as informações existentes,
# @ Somar números dentro do arquivo.
# OBS: Todas as informações que o usuário pode inserir terão que ser números 
# (Você precisa tratar os dados de entrada). 
from time import sleep
from sys import exit
op2= ''


while True:
    print('=+'*30)
    print('\n \t ------ ----- MENU ----- -----')
    print (''' 
    \t [ 1 ] Leia o Arquivo 
    \t [ 2 ] Insira novas informações 
    \t [ 3 ] Exclua as informações existentes
    \t [ 4 ] Somar os números de dentro do arquivo\n''')
    print('=+'*30)

    op = int(input('Digite a opção desejada : '))
    if op == 1:
        print(' \t .... Processando ...')
        sleep(1)
        
        print('3 ...')
        sleep(1)

        print('2 ..')
        sleep(1)
        
        print('1 .')
        sleep(1)
        
        print(f'''\n A opção desejada foi a [ {op}° ] \n
        * Irá Ler o Arquivo \n''')
    elif op == 2:
        print(' \t .... Processando ...')
        sleep(1)
        
        print('3 ...')
        sleep(1)

        print('2 ..')
        sleep(1)
        
        print('1 .')
        sleep(1)
        
        print(f'''\n A opção desejada foi a [ {op}° ] \n
        * Será Inserido novas informções no arquivo \n''')
    elif op == 3:
        print(' \t .... Processando ...')
        sleep(1)
        
        print('3 ...')
        sleep(1)

        print('2 ..')
        sleep(1)
        
        print('1 .')
        sleep(1)
        
        print(f'''\n A opção desejada foi a [ {op}° ] \n
        * Será excluído as informações já existentes do arquivo \n''')
    elif op == 4:
        print(' \t .... Processando ...')
        sleep(1)
        
        print('3 ...')
        sleep(1)

        print('2 ..')
        sleep(1)
        
        print('1 .')
        sleep(1)
        
        print(f'''\n A opção desejada foi a [ {op}° ] \n
        * Será somado os números de dentro do arquivo \n''')

    print('\n Deseja confirmar ou Quer tentar novamente ? ')
    print('''
        \t[ A ] Confirmar 
        \t[ B ] Tentar novamente \n''')
    
    op2 = ''
    op2 = input(' Digite a opção desejada: ').upper()
    
    while op2 == 'A':
        print ('...Processando ...')
        sleep(2) 
        if op == 1:
            with open ('Treino/info.txt', 'r') as arquivo:
                conteudo = arquivo.read()  
                print('--'*30)
                print(f'\n {conteudo}\n')
                print('--'*30)
        elif op == 2:
            with open ('Treino/info.txt', 'a') as arquivo: 
                
                while True :
                    novaFrase=input('Digite um número: ')
                    arquivo.write((novaFrase) + ' ')
                    continuar = input(' Deseja inserir outro número? [ S/N ]').upper()
                    if continuar == 'N':
                        print('--'*30)
                        print('\nConteúdo do arquivo txt foi alterado com sucesso .\n') 
                        print('--'*30) 
                        break
                    if continuar == 'S': 
                        continue
                    else:
                        break 
                                        
        elif op == 3:
            with open('Treino/info.txt', 'w') as arquivo:
                arquivo.write("")
            print('--'*30)
            print('\n Conteúdo do arquivo txt foi excluído com sucesso.\n')
            print('--'*30)            
        elif op == 4:
            with open ('Treino/info.txt','r') as arquivo:
                linhas = arquivo.readlines()
            soma = 0
            for linha in linhas:
                numeros = linha.strip().split()  
                soma += sum(map(int, numeros))
            print('--'*30)
            print(f'\n A soma dos números no arquivo é: {soma}\n')
            print('--'*30)
        saida = input(' Deseja continuar? [ S/N ]').upper()
        if saida == 'S':
            pass
        else:
            print('Finalizando ...')
            sleep(1)
            print('Obrigado(a) ^^')
            exit()
        break

        
    
