# Faça um programa que verifique se o site pudim.com.br
# está acessível no momento ou não:

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLERROR:
    print('O site Pudim não está acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    # print(site.read()) - > Mostra todo o conteúdo HTML dentro do site
