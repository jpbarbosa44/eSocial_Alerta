from bs4 import BeautifulSoup
import requests
import os 
from win10toast_click import ToastNotifier


if os.path.exists('./data') == False:
    os.mkdir('./data')
    file_leiaute = open('./data/leiaute.txt', 'w+', encoding="utf-8")
    file_NotasTecnicas = open('./data/NotasTecnicas.txt', 'w+', encoding="utf-8")
   

    toaster = ToastNotifier()
    r = requests.get('https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica')
    soup = BeautifulSoup(r.text, 'html.parser')


    leiautes_request = soup.find_all('a',{'class':'outstanding-link'})
    notasTecnicas_request = soup.find_all('a',{'class':'internal-link'})

    notasTecnicas = [nota.text for nota in notasTecnicas_request]
    leiautes = [leiaute.text for leiaute in leiautes_request]
   
 
    for i in leiautes:
        file_leiaute.writelines(f'{i}\n')

    for j in notasTecnicas:
        file_NotasTecnicas.writelines(f'{j}\n')

    file_leiaute.close()
    file_NotasTecnicas.close()

    with open('./data/leiaute.txt', 'r', encoding="utf-8") as texto:
        leiautes_old = texto.readlines()

    with open('./data/NotasTecnicas.txt', 'r', encoding="utf-8") as texto2:
        notasTecnicas_old = texto2.readlines()

else:
    browser = 'https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica'
  
    toaster = ToastNotifier()
    r = requests.get('https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica')
    soup = BeautifulSoup(r.text, 'html.parser')
    leiautes_request = soup.find_all('a',{'class':'outstanding-link'})
    notasTecnicas_request = soup.find_all('a',{'class':'internal-link'})

    notasTecnicas = [nota.text for nota in notasTecnicas_request]
    leiautes = [leiaute.text for leiaute in leiautes_request]

    with open('./data/leiaute.txt', 'r', encoding="utf-8") as texto:
        leiautes_old = texto.readlines()

    with open('./data/NotasTecnicas.txt', 'r', encoding="utf-8") as texto2:
        notasTecnicas_old = texto2.readlines()

    if len(notasTecnicas_old) == 0:
            file_NotasTecnicas = open('./data/NotasTecnicas.txt', 'w+', encoding="utf-8")
            for i in notasTecnicas:
                notasTecnicas_old.append(i)
                file_NotasTecnicas.writelines(f'{i}\n')
                     
    if len(leiautes_old) == 0:
            file_leiaute = open('./data/leiaute.txt', 'w+', encoding="utf-8")
            for j in leiautes:
                leiautes_old.append(j)
                file_leiaute.writelines(f'{j}\n')
                 

    if len(leiautes_old) == len(leiautes) and len(notasTecnicas_old) == len(notasTecnicas):    
        toaster.show_toast("Não houve alterações no eSocial", "teste notificação", icon_path='./assets/esocial.ico', duration=10)
    
    elif len(leiautes_old) != len(leiautes):
        file_leiaute = open('./data/leiaute.txt', 'w+', encoding="utf-8")
        for j in leiautes:
            leiautes_old.append(j)
            file_leiaute.writelines(f'{j}\n')
        toaster.show_toast("Houve uma alteração no eSocial", "leiaute", icon_path='./assets/esocial.ico', duration=10)
    
    elif  len(notasTecnicas_old) != len(notasTecnicas):
        file_NotasTecnicas = open('./data/NotasTecnicas.txt', 'w+', encoding="utf-8")
        for i in notasTecnicas:
            notasTecnicas_old.append(i)
            file_NotasTecnicas.writelines(f'{i}\n')
        toaster.show_toast("Houve uma alteração no eSocial", "notas técnicas", icon_path='./assets/esocial.ico', duration=10)
    
    else:
        file_leiaute = open('./data/leiaute.txt', 'w+', encoding="utf-8")
        for j in leiautes:
            leiautes_old.append(j)
            file_leiaute.writelines(f'{j}\n')
        
        file_NotasTecnicas = open('./data/NotasTecnicas.txt', 'w+', encoding="utf-8")
        for i in notasTecnicas:
            notasTecnicas_old.append(i)
            file_NotasTecnicas.writelines(f'{i}\n')
        toaster.show_toast("Houve uma alteração no eSocial", "teste notificação", icon_path='./assets/esocial.ico', duration=10)