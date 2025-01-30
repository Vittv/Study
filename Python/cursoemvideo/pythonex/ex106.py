from time import sleep
import sys

GREEN = '\033[42m'
BLUE = '\033[44m'
NEGATIVE = '\033[7m'
RESET = '\033[0m' 

def colored_print(text, color):
    print(color + text + RESET)

def PyHelp():
    while True:

        colored_print('~' * len('  SISTEMA DE AJUDA PyHELP  '), GREEN)
        colored_print('  SISTEMA DE AJUDA PYHELP  ')
        colored_print('~' * len('  SISTEMA DE AJUDA PyHELP  '), GREEN)

        prompt = input('Função ou Biblioteca > ')

        sleep(1)

        colored_print('~' * len(f"Acessando o manual do comando '{prompt}' "), BLUE)
        colored_print(f"Acessando o manual do comando '{prompt}' ")
        colored_print('~' * len(f"Acessando o manual do comando '{prompt}' "), BLUE)

        sleep(1)

        if prompt.lower() == 'fim':
            print('Encerrando o sistema de ajuda.')
            break
           
        colored_print(help(prompt), NEGATIVE)


PyHelp()
