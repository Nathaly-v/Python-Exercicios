# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = (float (input ('Escreva uma distância:')))

km= metros  * 0.001
hm= metros  * 0.01
dam= metros * 0.1 
dm= metros  * 10
cm= metros  * 100
mm= metros  * 1000 

print (f' Uma distância em metros {metros} \n A medida de {metros} corresponde a \n {km} Km \n {hm} Hm \n {dam:.2f} Dam \n {dm} Dm \n {cm} Cm \n {mm} Mm')