from bs4 import BeautifulSoup
import requests
import os 
from win10toast import ToastNotifier


os.mkdir('./data')
file_leiaute = open('./data/leiaute.txt', 'w+', encoding="utf-8")
file_NotasTecnicas = open('./data/NotasTecnicas.txt', 'w+', encoding="utf-8")

leiautes = []
notasTecnicas = []


toaster = ToastNotifier()
r = requests.get('https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica')
soup = BeautifulSoup(r.text, 'html.parser')


leiautes_request = soup.find_all('a',{'class':'outstanding-link'})
notasTecnicas_request = soup.find_all('a',{'class':'internal-link'})


for nota in notasTecnicas_request:
    notasTecnicas.append(nota.text)

for documento in leiautes_request:
    leiautes.append(documento.text)


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


if len(leiautes_old) == len(leiautes) and len(notasTecnicas_old) == len(notasTecnicas):
     toaster.show_toast("Não houve alterações no eSocial", "teste notificação", icon_path='./assets/esocial.ico', duration=10)
else:
    toaster.show_toast("Houve uma alteração no eSocial", "teste notificação", icon_path='./assets/esocial.ico', duration=10)
