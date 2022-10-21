import os

from main import Alerta

if __name__ == '__main__':
    alerta = Alerta()

    if os.path.exists('./data') == False:
        alerta.criaDiretorio()
    
    
    alerta.getRequest()
    alerta.scrapy()
    alerta.populaListas()
    alerta.populaListaAntigaLeiaute()
    alerta.verificaSeLeiautesEstaoVazios()
    alerta.populaListaAntigaLeiaute()
    alerta.verificaSeNotasTecnicasEstaoVazias()
    alerta.populaListaAntigaNotasTecnicas()
    alerta.realizaAsValidacoes()
