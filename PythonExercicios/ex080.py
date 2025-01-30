lista = []

n1 = int(input('Digite um valor: '))
lista.append(n1)

n2 = int(input('Digite um valor: '))
if n2 <= n1:
    lista.insert(0, n2)
else:
    lista.append(n2)

n3 = int(input('Digite um valor: '))
if n3 <= lista[0]:
    lista.insert(0, n3)
elif n3 >= lista[-1]:
    lista.append(n3)
else:
    for i in range(len(lista) - 1):
        if lista[i] <= n3 <= lista[i + 1]:
            lista.insert(i + 1, n3)
            break

n4 = int(input('Digite um valor: '))
if n4 <= lista[0]:
    lista.insert(0, n4)
elif n4 >= lista[-1]:
    lista.append(n4)
else:
    for i in range(len(lista) - 1):
        if lista[i] <= n4 <= lista[i + 1]:
            lista.insert(i + 1, n4)
            break

n5 = int(input('Digite um valor: '))
if n5 <= lista[0]:
    lista.insert(0, n5)
elif n5 >= lista[-1]:
    lista.append(n5)
else:
    for i in range(len(lista) - 1):
        if lista[i] <= n5 <= lista[i + 1]:
            lista.insert(i + 1, n5)
            break

print(lista)