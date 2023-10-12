import requests
from bs4 import BeautifulSoup

class Site:
    def __init__ (self, opcao:str):
        self.opcao = opcao
        self.news = {}

    def update_news(self):
        if self.opcao.lower() == 'globo':
            url = 'https://www.globo.com/' 
            headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
            page = requests.get(url, headers=headers)

            resposta = page.text
            soup = BeautifulSoup(resposta, 'html.parser')
            
            noticias = soup.find_all('a')
            tg_class1 = 'post__title'
            tg_class2 = 'post-multicontent__link--title__text'


            news_dict_globo = {}
            for noticia in noticias:
                if noticia.h2 != None:
                    if tg_class1 in noticia.h2.get("class") or tg_class2 in noticia.h2.get("class"):
                        news_dict_globo[noticia.h2.text] = noticia.get('href')
                          
            self.news = news_dict_globo

        elif self.opcao.lower() == 'cnn':
            url = 'https://www.cnnbrasil.com.br/'
            headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}
            page = requests.get(url, headers=headers)

            resposta = page.text
            soup = BeautifulSoup(resposta, 'html.parser')

            noticias = soup.find_all('a')
            tg_class1 = 'block__news__title'

            news_dict_cnn = {}
            for noticia in noticias:
                if noticia.h2 != None: 
                    if tg_class1 in noticia.h2.get("class"):
                        news_dict_cnn[noticia.h2.text] = noticia.get('href')

                if noticia.h3 != None: 
                    if tg_class1 in noticia.h3.get("class"):
                        news_dict_cnn[noticia.h3.text] = noticia.get('href')

                if noticia.h4 != None: 
                    if tg_class1 in noticia.h4.get("class"):
                        news_dict_cnn[noticia.h4.text] = noticia.get('href')

            self.news = news_dict_cnn



                


        
        




