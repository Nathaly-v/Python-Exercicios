#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.


while True:
    opcao = int (input(' Quer ver a tabuada de qual valor ? '))
    if opcao < 0:
        print(' PROGRAMA TABUADA ENCERRADO. volte sempre !')
        break 
    print ('-'*50)
    for tabuada in range (1, 11):
        vezes = tabuada * opcao   
        print (f'{opcao} x {tabuada} = {vezes}')
    print ('-'*50) 
   