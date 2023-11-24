# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario= float (input( ' - Qual é o salário do funcionário : ' ))


valor=  salario * 110/100
valor2= salario * 115/100

if salario >= 1250.00 :
    print (f'Quem ganhava R$ {salario}, passa a ganhar R$ {valor} agora. ')
    
else:
    print (f'Quem ganhava R$ {salario}, passa a ganhar R$ {valor2} agora. ')