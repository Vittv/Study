'''lanche = ['hambúrguer', 'suco', 'pizza', 'pudim']
lanche.append('cookie')
if 'pizza' in lanche:
    del lanche[2]    # Três formas de remover elementos de uma lista
    lanche.pop(2)    # Pode usar qualquer uma, mas, .pop é mais usado para remover o último item
    lanche.remove('pizza')
    if 'pizza' in lanche:
        lanche.remove('pizza')

valores = list(range(4, 11))
valores2 = [8, 2, 5, 4, 9, 3, 0]
valores.sort()
valores.sort(reverse=True)
len(valores)  # = 7'''

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()  # [1, 2, 3, 5, 7]
num.sort(reverse=True)  # [7, 5, 3, 2, 1]
num.insert(2, 0)  # [7, 5, 0, 3, 2, 1]
num.pop()  # [7, 5, 0, 3, 2]  remove o último item, ao menos que especificado em ()
num.remove(2)  # vai remover apenas o primeiro 2 que achar na lista
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Esta lista tem {len(num)} elementos.')

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')
print('Cheguei ao final da lista.')

a = [2, 3, 4, 7]
b = a  # iguala as duas listas, mesmo que vc mude seus elementos
b = a[:]  # dessa forma vc copia de forma correta
b[2] = 8  # ao fazer isso, ambas as listas a e b mudaram seu 4 para um 8 pois b = a
print(f'Lista a: {a}')
print(f'Lista b: {b}')