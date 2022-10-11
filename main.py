from bs4 import BeautifulSoup
import requests
import os 
from win10toast import ToastNotifier

class Alerta():
    def scraping(self):
        self.toaster = ToastNotifier()
        r = requests.get('https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica')
        soup = BeautifulSoup(r.text, 'html.parser')
        leiautes_request = soup.find_all('a',{'class':'outstanding-link'})
        notasTecnicas_request = soup.find_all('a',{'class':'internal-link'})

    def populaListas(self):
        leiautes = []
        notasTecnicas = []
        for nota in self.notasTecnicas_request:
            notasTecnicas.append(nota.text)

        for documento in self.leiautes_request:
            leiautes.append(documento.text)

    def salvaLista(self, file_NotasTecnicas, file_leiaute):
        for i in self.leiautes:
            file_leiaute.writelines(f'{i}\n')

        for j in self.notasTecnicas:
            file_NotasTecnicas.writelines(f'{j}\n')
        
        self.file_leiaute.close()
        self.file_NotasTecnicas.close()
    
    def populaListaAntiga(self):
        with open('./data/leiaute.txt', 'r', encoding="utf-8") as texto:
            self.leiautes_old = texto.readlines()

        with open('./data/NotasTecnicas.txt', 'r', encoding="utf-8") as texto2:
            self.notasTecnicas_old = texto2.readlines()