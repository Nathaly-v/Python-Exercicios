# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
normal = "\033[0m" # to come back to default
 
# Número primo é todo aquele que é divisivel por {1} e {ele mesmo}

for _ in range(1, 10 + 1):
    num = int(input(' Digite um número : '))
    cont=0
    for n1 in range(1,num + 1):
        if num % n1 == 0:
            print(purple + f'{n1} ', end= ' ' + normal)    
            cont += 1      
        else: 
            print (yellow + f'{n1} ', end= ' ' + normal)  
    if cont > 2 or cont <= 1:
        print(purple + f'\no número {num} foi divisível {cont} vezes \n Não é PRIMO ')
    else :
        print(f'\no número {num} foi divisível {cont} vezes \n É PRIMO'+ normal)
    

