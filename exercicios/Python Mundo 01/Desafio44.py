# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# – à vista dinheiro/cheque: 10% de desconto

# – à vista no cartão: 5% de desconto

# – em até 2x no cartão: preço normal 

# – 3x ou mais no cartão: 20% de juros

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
normal = "\033[0m" # to come back to default

from time import sleep

print (('='* 10) + purple + ' LOJA DA NATHY  ' + normal + ('='* 10))

preço = float (input ( yellow + ' Preço das COMPRAS : R$ '+ normal))

print (purple +' FORMAS DE PAGAMENTO : '+ normal)

print (yellow + ' [ 1 ] à vista DINEHIRO / CHEQUE ')
print (' [ 2 ] à vista no CARTÃO ')
print (' [ 3 ] 2x no CARTÃO ')
print (' [ 4 ] 3x ou mais no CARTÃO ' + normal)

opçao= int (input(' Qual é a opção ? '))

dinheiro = preço - ( preço * 10 /100)
cartao= preço - ( preço * 5 /100)
cartao2x= preço
cartao3x= preço * 120 / 100
parcela = (0 or 24)
parcela2 = preço / 2

if opçao == 1 :
    print (f' Sua compra de R$ {preço} vai custar R$ {dinheiro} no final. ')
    
elif opçao == 2 :
    print (f' Sua compra de R$ {preço} vai custar R$ {cartao} no final. ')
    
elif opçao == 3 : 
    
    print (f' Sua compra será parcelada 2X de R${parcela2 :.2f} SEM JUROS !')
    print (f' Sua compra de R$ {preço} vai custar R$ {cartao2x} no final. ')
    
    
elif opçao  == 4 :
    
    parcela= int (input ( ' Quantas parcelas ? '))
    vparcela=  cartao3x/parcela
    print (f' Sua compra será parcelada { parcela }X de R${vparcela :.2f} COM JUROS !')
    print (f' Sua compra de R$ {preço} vai custar R$ {cartao3x} no final. ')
    
else:
    preço = opçao
    print (red +' OPÇÃO INVÁLIDA DE PAGAMENTO ! Tente novamente ' + normal)

