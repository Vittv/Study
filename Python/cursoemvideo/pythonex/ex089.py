# Faça um programa de boletim:

lista = []
media = 0

while True:

    dado = []
    nome = str(input('Nome: ')).strip().capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    dado.append(nome)
    dado.append(nota1)
    dado.append(nota2)
    lista.append(dado)
    
    if escolha in 'N':
        break

print('='*25)
print('No.   NOME         MEDIA')
print('-'*25)

numal = 1
n = 0

for aluno in lista:

    media = (aluno[1] + aluno[2]) / 2
    print(f'{numal:<6}{aluno[0]:<14}{media:.1f}')  
    numal += 1

while True:

    n = int(input('Mostrar notas de qual aluno? [999 para interromper] '))

    if n == 999:
        print('PROGRAMA ENCERRADO')
        break

    if 1 <= n <= len(lista):
        alunoescolhido = lista[n - 1]
        print(f'Notas de {alunoescolhido[0]}: {alunoescolhido[1]}, {alunoescolhido[2]}')
    else:
        print('Número de aluno inválido. Tente novamente.')