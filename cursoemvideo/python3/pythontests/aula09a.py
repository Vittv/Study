'''frase = 'Curso em Vídeo Python'
print(frase[9::3])
len(frase)
frase.count('o')
print(len(frase))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('Android')) #since this word doesn't exist in the string, it will give you -1 as value
#all of this should give you: 21, 1, 11, -1
'Curso'in frase
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
frase2 = '   Aprenda Python  '
print(frase2.strip()) #removes unnecessary space
print(frase2.rstrip()) #removes only the right space
print(frase2.lstrip()) #removes only the left space
print(frase.split())
print('-'.join(frase))'''
frase = 'Curso em Vídeo Python'
print(frase[::2])
print('''aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa''')
print('Curso' in frase)
