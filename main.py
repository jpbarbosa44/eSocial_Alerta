from bs4 import BeautifulSoup
import requests
import os 
from win10toast import ToastNotifier

class Alerta():
    
    def timer():
        ...
    def driver():
        ...
    def criaArquivos(self):
        os.mkdir('./data')
        self.file_leiaute = open('./data/leiaute.txt', 'w+', encoding="utf-8")
        self.file_NotasTecnicas = open('./data/NotasTecnicas.txt', 'w+', encoding="utf-8")
    def getRequest(self):
        self.r = requests.get('https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica')
        
    def scrapy(self):
        soup = BeautifulSoup(self.r.text, 'html.parser')
        self.leiautes_request = soup.find_all('a',{'class':'outstanding-link'})
        self.notasTecnicas_request = soup.find_all('a',{'class':'internal-link'})

    def populaListas(self):
        self.notasTecnicas = [nota.text for nota in self.notasTecnicas_request]
        self.leiautes = [leiaute.text for leiaute in self.leiautes_request]

    def populaArquivos(self):
        for i in self.leiautes:
            self.file_leiaute.writelines(f'{i}\n')

        for j in self.notasTecnicas:
            self.file_NotasTecnicas.writelines(f'{j}\n')
        
        self.file_leiaute.close()
        self.file_NotasTecnicas.close()
    
    def populaListaAntiga(self):
        with open('./data/leiaute.txt', 'r', encoding="utf-8") as texto:
            self.leiautes_old = texto.readlines()

        with open('./data/NotasTecnicas.txt', 'r', encoding="utf-8") as texto2:
            self.notasTecnicas_old = texto2.readlines()
    
    def verificaSeNotasTecnicasEstaoVazias(self):
         if len(self.notasTecnicas_old) == 0:
            file_NotasTecnicas = open('./data/NotasTecnicas.txt', 'w+', encoding="utf-8")
            for i in self.notasTecnicas:
                self.notasTecnicas_old.append(i)
                file_NotasTecnicas.writelines(f'{i}\n')
    
    def verificaSeLeiautesEstaoVazios(self):
        if len(self.leiautes_old) == 0:
            file_leiaute = open('./data/leiaute.txt', 'w+', encoding="utf-8")
            for j in self.leiautes:
                self.leiautes_old.append(j)
                file_leiaute.writelines(f'{j}\n')