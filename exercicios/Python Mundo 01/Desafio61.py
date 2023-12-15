# Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print(' Gerador de PA')
print('-='*30)

termo = int(input( 'Primeiro termo : '))
razao =  int(input( 'Razão DA PA : '))
cont = 0

while True:
    for number in range (termo, 999, razao):
        if cont ==10:
            break
        cont = cont +1
        print(f'{number}',end = ' ↦ ')
    break
print(' FIM! ')
    