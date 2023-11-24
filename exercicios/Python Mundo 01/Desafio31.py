#  Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

dist= float (input (' Qual é a distância da sua viagem ? '))

preço= (dist) * 0.50
preço2=(dist) * 0.45

if dist <= 200 :
    print (f' O preço de sua passagem será de : R$ {preço}')
    
else:
    print (f' O preço de sua passagem será de : R$ {preço2} ')