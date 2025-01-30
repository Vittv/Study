# Faça um programa que verifique se o site pudim.com.br
# está acessível no momento ou não:

import requests

def check_website_access(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The website {url} is accessible.")
        else:
            print(f"Failed to access the website {url}. Status code: {response.status_code}")
    except requests.ConnectionError:
        print(f"Failed to connect to the website {url}. Please check your internet connection.")


website_url = 'http://pudim.com.br'
check_website_access(website_url)
