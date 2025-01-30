# Faça um programa que leia nome e média de um aluno,
# mostrando se o mesmo foi aprovado ou reprovado:

aluno = {}
aluno['Nome'] = str(input('Digite o nome: ')).capitalize()
aluno['Média'] = float(input('Digite a média: '))

if aluno['Média'] >= 6:
    aluno['Situação'] = 'aprovado'
    print(f'Aluno(a) {aluno["Nome"]} {aluno["Situação"]} com média {aluno["Média"]}.')

else:
    aluno['Situação'] = 'reprovado'
    print(f'Aluno(a) {aluno["Nome"]} {aluno["Situação"]} com média {aluno["Média"]}.')