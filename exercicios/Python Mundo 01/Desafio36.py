# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

vcasa= float (input(' - Valor da Casa : '))
scomprador= float (input(' - Salário do comprador : '))
anosf= int (input(' - Quantos anos de financiamento : '))

mensal =  vcasa / ( anosf * 12 )

aum= scomprador * 0.30

if mensal >= aum:
    
    print (f' Para pagar uma casa de {vcasa}, em {anosf} anos, a prestação será de {mensal :.2f} mensais \n Empréstimo NEGADO !  ')
    
else:
    
    print(f' Para pagar uma casa de {vcasa}, em {anosf} anos, a prestação será de {mensal :.2f} mensais  \n Empréstimo CONCEDIDO !  ')