# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# – EQUILÁTERO: todos os lados iguais

# – ISÓSCELES: dois lados iguais, um diferente

# – ESCALENO: todos os lados diferentes

a = int(input(' - Primeiro segmento : '))
b = int(input(' - Segundo segmento : '))
c = int(input(' - Terceiro segmento : '))

if (a + b) > c and (a + c) > b and (b + a ) > c and (b + c ) > a and (c + a) > b and (c + b) > a :  
    print (' Os segmentos acima PODEM FORMAR um triângulo : ', end = '')
    
# equilátero = iguais 

    if a == b and a == c and b == a and b == c and c == a and c == b :
        print (' EQUILÁTERO !')


# escaleno = todos os lados diferentes

    elif a != b and a != c and b != a and b != c and c != a and c != b :
        print (' ESCALENO !')
 
# isósceles = 2 lados iguais 1 diferente

    else :
        print (' ISÓCELES !')

else :
    print (' Não PODEM FORMAR um triângulo. ')