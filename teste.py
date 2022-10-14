from bs4 import BeautifulSoup
import requests
import os 
from win10toast_click import ToastNotifier

from main import Alerta

if __name__ == '__main__':
    alerta = Alerta()
    alerta.getRequest()
    alerta.criaArquivos()
    alerta.scrapy()
    alerta.populaListas()
    alerta.populaArquivos()
    alerta.populaListaAntiga()