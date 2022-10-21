from bs4 import BeautifulSoup
import requests
import os 
import asyncio
from win10toast_click import ToastNotifier


class Alerta():
    notasTecnicas_old = []
    leiautes_old = []

    def timer():
        ...
    def driver():
        ...
    def criaDiretorio(self):
        os.mkdir('./data')
        self.file_leiaute = open('./data/leiaute.txt', 'w+', encoding="utf-8")
        self.file_NotasTecnicas = open('./data/NotasTecnicas.txt', 'w+', encoding="utf-8")
    
    def criaArquivoNotasTecnicas(self):
        open('./data/leiaute.txt', 'w+', encoding="utf-8")

    def criaArquivoLeiautes(self):
        open('./data/leiaute.txt', 'w+', encoding="utf-8")

    def getRequest(self):
        self.r = requests.get('https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica')
        
    def scrapy(self):
        soup = BeautifulSoup(self.r.text, 'html.parser')
        self.leiautes_request = soup.find_all('a',{'class':'outstanding-link'})
        self.notasTecnicas_request = soup.find_all('a',{'class':'internal-link'})

    def populaListas(self):
        self.notasTecnicas = [nota.text for nota in self.notasTecnicas_request]
        self.leiautes = [leiaute.text for leiaute in self.leiautes_request]

    def populaArquivoLeiautes(self):
        for i in self.leiautes:
            self.file_leiaute.writelines(f'{i}\n')
        
    def populaArquivoNotasTecnicas(self):
        for j in self.notasTecnicas:
            self.file_NotasTecnicas.writelines(f'{j}\n')
        self.file_NotasTecnicas.close()    
    
    def populaListaAntigaLeiaute(self):
        with open('./data/leiaute.txt', 'r', encoding="utf-8") as texto:
            self.leiautes_old = texto.readlines()
       
        
    def populaListaAntigaNotasTecnicas(self):
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
    
    
    def realizaAsValidacoes(self):
        toaster = ToastNotifier()
        if len(self.leiautes_old) == len(self.leiautes) and len(self.notasTecnicas_old) == len(self.notasTecnicas):    
            toaster.show_toast("Não houve alterações no eSocial", "teste notificação", icon_path='./assets/esocial.ico', duration=10)

        elif len(self.leiautes_old) != len(self.leiautes):
            with open('./data/leiaute.txt', 'w+', encoding="utf-8") as file_nt:
                file_nt.truncate(0)
                file_nt.seek(0)
            
            self.file_leiaute = open('./data/leiaute.txt', 'w+', encoding="utf-8")
            
            for j in self.leiautes:
                self.leiautes_old.append(j)
                self.file_leiaute.writelines(f'{j}\n')
            toaster.show_toast("Houve uma alteração no eSocial", "leiaute", icon_path='./assets/esocial.ico', duration=10)
        
        elif  len(self.notasTecnicas_old) != len(self.notasTecnicas):
            with open('./data/NotasTecnicas.txt', 'w+', encoding="utf-8") as file_leiaute:
                file_leiaute.truncate(0)
                file_leiaute.seek(0)
            
            self.file_NotasTecnicas = open('./data/NotasTecnicas.txt', 'w+', encoding="utf-8")
            
            for i in self.notasTecnicas:
                self.notasTecnicas_old.append(i)
                self.file_NotasTecnicas.writelines(f'{i}\n')
            toaster.show_toast("Houve uma alteração no eSocial", "notas técnicas", icon_path='./assets/esocial.ico', duration=10)
        