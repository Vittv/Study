# Faça um programa que mostre diversas informações sobre a tabela do brasileirão:
times = ('Palmeiras', 'Grêmio', 'Atlético-MG', 'Flamengo', 'Botafogo', 'Bragantino', 'Fluminense',
         'Fluminense', 'Athletico-PR', 'Internacional', 'Fortaleza', 'São Paulo', 'Cuiabá', 'Corinthians',
         'Cruzeiro', 'Vasco da Gama', 'Bahia', 'Santos', 'Goiás', 'Coritiba', 'América-MG')
print(f'5 primeiros colocados: {times[0:5]}')
print(f'Últimos 4 colocados: {times[-4:]}')
print(f'Em ordem alfabética: {sorted(times)}')
print(f'O time {times[14]} está na {times.index('Cruzeiro')+1}ª posição')
