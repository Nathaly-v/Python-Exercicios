# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras=(
    ('APRENDER'),
    ('PROGRAMAR'),
    ('LINGUAGEM'),
    ('PYTHON'),
    ('CURSO'),
    ('GRATIS'),
    ('ESTUDAR'),
    ('PRATICAR'),
    ('TRABALHAR'),
    ('MERCADO'),
    ('PROGRAMADOR'),
    ('FUTURO')
)

for item in palavras:
    print(f'Na palavra {item} temos: ', end =' ')
          
    for letra in range (0, (len(item))):
        if item[letra] == 'A':
           print(f'{item[letra]} ', end =' ')
        if item[letra] == 'E':
           print(f'{item[letra]} ', end =' ')
        if item[letra] == 'I':
           print(f'{item[letra]} ', end =' ')
        if item[letra] == 'O':
           print(f'{item[letra]} ', end =' ')
        if item[letra] == 'U':
           print(f'{item[letra]} ', end =' ')
    print('')
    