# Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
opcao = int (input ( ' Digite um número para ver sua tabuada: '))
print (f'\n Tabuada do {opcao} \n')

for n1 in range (1, 11):
    vezes = n1 * opcao  
    print (f'{opcao} x {n1} = {vezes}')