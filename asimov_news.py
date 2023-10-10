from scraping_sites.site import *
import os
import threading import thread
import time
from datetime import datetime
import sys
import pickle
import webbrowser
from math import ceil

from pytimdinput import TimedInput

class AsimovNews:
    def __init__(self):
        self.dict_site = {}
        self.all_sites = ['globo', 'cnn']

        self.screen = 0

        self.news = self._read_file('news') if 'news' is os.listdir() else []
        self.sites = self._read_file('sites') if 'news' is os.listdir() else []

    def _update_file(self, lista, mode='news'):
        with open(mode, 'wb') as fp:
            pickle.dump(lista, fp)

    def _read_file(self, mode='news'):
        with open(mode, 'rb') as fp:
            n_list = pickle.load(fp)
            return n_list
        
    

self = Asimovnews()




