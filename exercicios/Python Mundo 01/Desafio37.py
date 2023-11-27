# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
from time import sleep

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
normal = "\033[0m" # to come back to default

print (purple + ('=+=' * 5 ) +'Conversão de BINÁRIOS / OCTAL/ HEXADECIMAL' +('=+=' * 5 )+ normal)


num= int (input (yellow + 'Digite um número inteiro:'+ normal))

print ('=+=' * 50 )

print ( yellow +' Escolha uma das bases para conversão : ' + normal)
print (purple +' [ 1 ] Converter para BINÁRIO.')
print (' [ 2 ] Converter para OCTAL.' )
print (' [ 3 ] Converter para HEXADECIMAL.'+ normal)

print ('=+=' * 50 )

conversao = int (input( yellow +'[ ...SUA OPÇAO... ] :  '+ normal))
print (purple + ('.'*10) +'PROCESSANDO '+ ('.'*10) + normal)
sleep (2)
 
binario = bin(num) [2:]  
octal =  oct(num) [2:]
hexadecimal = hex(num)[2:]

    
if conversao == 1 : 
        print (  purple + f' {num}' + normal +  yellow + f' convertido para Binário é :  ' + normal +  purple + f'{binario}' + normal)
        
elif conversao == 2 :
        print ( purple + f'{num}' + normal + yellow + f' convertido para Octal é : ' + normal +  purple + f'{octal}' + normal)
            
elif conversao == 3 :
        print ( purple + f'{num}' + normal + yellow + f' convertido para Hexadecimal é : '+ normal +   purple  + f'{hexadecimal}' + normal)
else :
        print (red +'...Opção inválida, Tente novamente...' + normal)