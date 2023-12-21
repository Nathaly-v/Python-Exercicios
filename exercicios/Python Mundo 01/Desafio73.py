# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.

times = ('Palmeiras','Grêmio','Atlético-MG','Flamengo','Botafogo',	
'Bragantino','Fluminense', 'Athletico-PR','Internacional','Fortaleza',
'SãoPaulo','Cuiabá','Corinthians','Cruzeiro','Vasco','Bahia','Santos','Goiás',
'Coritiba','América-MG')
posicao= times.index('Athletico-PR')
    
print('-='*50)
print(f'Lista de Times do Brasileirão de 2023: {times}')
print('-='*50)
print(f' Os 5 primeiros times são: {times[0:5]}')
print('-='*50)
print(f' Os últimos  4 times são: {times[16:]}')
print('-='*50)
print(f' Times em ordem alfabética: {tuple(sorted(times))}')
print('-='*50)
print(f' O time do Athletico-PR,está na {posicao+1}° posição')
print('-='*50)