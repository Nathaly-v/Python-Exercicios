# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print(' Gerador de PA')
print('-='*30)

termo = int(input( 'Primeiro termo : '))
razao =  int(input( 'Razão DA PA : '))
cont = 1
contTotal=0
maisTermo = 1  
while cont <= 10:
    print(f'{termo}',end = ' ↦ ')
    termo = termo + razao
    cont = cont + 1          
    contTotal = contTotal + 1
print('PAUSA \n')
while maisTermo != 0:
    maisTermo= int(input(' Quantos termos você quer mostrar a mais ? '))
    cont = 1
    while cont <= maisTermo:
        print(f'{termo}',end = ' ↦ ')
        termo = termo + razao
        cont = cont + 1
        contTotal = contTotal + 1
    if maisTermo != 0:
        print('PAUSA')
print (f'Progressão finalizada com {contTotal} termos mostrados')
      
    
