import os
import time
import requests
from bs4 import BeautifulSoup
from timeit import default_timer as timer
from PyQt5 import QtCore, QtGui, QtWidgets

class Real_Time(QtCore.QThread):
    power = QtCore.pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.homeapge = 'https://e-hentai.org/home.php'
        self.cookie = None
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
        self.powers = '0 / 0'

    def build_config(self, config, powers):
        self.cookie = config
        self.headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                        'Accept-Encoding' :'gzip, deflate, br',
                        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
                        'Cache-Control': 'max-age=0',
                        'Connection': 'keep-alive',
                        'Cookie': 'yay=louder; ipb_member_id={}; ipb_pass_hash={}; ipb_session_id={}; igneous={}; sk={}'.format(self.cookie['ipb_member_id'], self.cookie['ipb_pass_hash'], self.cookie['ipb_session_id'], self.cookie['igneous'], self.cookie['sk']),
                        'Host': 'exhentai.org',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'none',
                        'Sec-Fetch-User': '?1',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.121 Safari/537.36 Vivaldi/2.8.1664.44'
                        }
        self.powers = powers

    def run(self):
        last = self.powers
        while 1:
            try:
                self.sleep(5)
                resqonse = requests.get('https://e-hentai.org/home.php', cookies=self.cookie, headers={'User-Agent':self.user_agent})
                data = BeautifulSoup(resqonse.text, 'lxml')
                if len(data) !=0:
                    points = data.find_all('strong', limit=2)
                    self.power.emit(last)
                    last = '{} / {}'.format(int(points[0].text), int(points[1].text))

            except:
                pass

