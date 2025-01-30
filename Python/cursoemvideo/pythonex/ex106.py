from time import sleep
import sys

def PyHelp():
    while True:

        print('~' * len('  SISTEMA DE AJUDA PyHELP  '))
        print('  SISTEMA DE AJUDA PYHELP  ')
        print('~' * len('  SISTEMA DE AJUDA PyHELP  '))
        sys.stdout.flush()

        prompt = input('Função ou Biblioteca > ')
        sys.stdout.flush()

        print('~' * len(f"Acessando o manual do comando '{prompt}' "))
        print(f"Acessando o manual do comando '{prompt}' ")
        print('~' * len(f"Acessando o manual do comando '{prompt}' "))
        sys.stdout.flush()

        sleep(0.5)

        if prompt.lower() == 'fim':
            print('Encerrando o sistema de ajuda.')
            break
           
        print(help(prompt))
        sys.stdout.flush()


PyHelp()
