def notas(*nota, sit=False):

    '''-> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma'''

    notas = {}
    notas['total'] = len(nota)
    notas['maior'] = max(nota)
    notas['menor'] = min(nota)
    notas['média'] = sum(nota) / notas['total']

    if sit:

        if notas['média'] < 6:
            notas['situação'] = 'RUIM'
        
        elif 6 < notas['média'] < 7:
            notas['situação'] = 'RAZOÁVEL'

        elif notas['média'] >= 7:
            notas['situação'] = 'BOA'

        return notas
    


    elif not sit:
        return notas


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)