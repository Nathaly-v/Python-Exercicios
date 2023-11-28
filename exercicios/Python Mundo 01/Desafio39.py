 # Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. 

nasc = int (input(' - Ano de nascimeto : '))

anos = 2023 - nasc 
menor = 18 - anos
maisv = anos - 18
maior = nasc + 18


if anos == 18 :
    print (f' Quem nasceu em {nasc} tem anos {anos} em 2023. ')
    print (' Você tem que se alistar IMEDIATAMENTE ! ')

elif anos < 18 :
    print (f' Quem nasceu em {nasc} tem anos {anos} em 2023. ')
    print (f' Ainda faltam {menor} anos para o alistamento. ')
    print (f' Seu alistamento será em {maior}')
    
elif anos > 18 :
    print (f' Quem nasceu em {nasc} tem  anos {anos} em 2023. ')
    print (f'Você já deveria ter se alistado há {maisv} anos. ')
    print (f'Seu alistamento foi em {maior}')
