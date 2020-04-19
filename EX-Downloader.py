# encoding=utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_main_ver2 import Ui_MainWindow
from ex_v4 import thread
import numpy as np
from PIL import Image
import sys
import os
import json
from real_time import Real_Time

class Main_Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main_Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.setFixedSize(800,574)
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('D:/ex_hentai/ver3/icon_0.ico'))
        self.ui.dst_text.setText('{}'.format(os.getcwd()))
        self.last_image='D:/ex_hentai/ver3/cover.jpg'
        self.hentai = thread()
        self.rt = Real_Time()
        self.config = {
            'ipb_member_id':None,
            'ipb_pass_hash':None,
            'ipb_session_id':None,
            'igneous':None,
            'sk':None
            }
        self.memory = {
            'favs':[],
            'now_fav':-1,
            'tabs':[],
            'now_tab':-1,
            'books':[],
            'now_book':-1,
            'pages':[],
            'now_page':-1,
            'pause':0
            }
        self.flag_pause = 0
        self.powers = '0 / 0'
        self.error_image = np.array(Image.open('D:/ex_hentai/ver3/error.JPG'))
        self.folder=os.getcwd()

        # Bottom
        self.ui.botton_load_config.clicked.connect(self.is_load_config)
        self.ui.botton_start.clicked.connect(self.is_start)
        self.ui.botton_exit.clicked.connect(self.exit)
        self.ui.botton_folder.clicked.connect(self.open_folder)
        self.ui.botton_pause.clicked.connect(self.is_pause)
        self.ui.botton_open_folder.clicked.connect(self.current_folder)
        # Hentai
        self.hentai.now_tag.connect(self.put_tag)
        self.hentai.now_book.connect(self.put_title)
        self.hentai.book_config.connect(self.put_book_config)
        self.hentai.now_page.connect(self.put_pages)
        self.hentai.msg.connect(self.recv)
        self.hentai.image.connect(self.put_Cover)
        self.hentai.memory.connect(self.is_memory)
        self.hentai.folder.connect(self.get_folder)
        self.hentai.bad.connect(self.is_bad_conn)
        self.rt.power.connect(self.power)

    def exit(self):
        sys.exit(app.exec_())

    def is_start(self):
        self.ui.botton_folder.setEnabled(False)
        self.ui.botton_start.setEnabled(False)
        self.ui.botton_load_config.setEnabled(False)
        self.hentai.start()
        self.rt.start()

    def is_load_config(self):
        config = {
            'ipb_member_id':'None',
            'ipb_pass_hash':'None',
            'ipb_session_id':'None',
            'igneous':'None',
            'sk':'None'
            }
        if os.path.isfile('config.json'):
            with open('config.json','r') as f:
                jf = json.load(f)
                self.load_config(jf)
        else:
            self.recv('\n*** Config Creating... ***\n*** Please check it... ***\n')
            with open('config.json','w') as f:
                json.dump(config,f)

    def load_config(self, config):
        self.config['ipb_member_id'] = config['ipb_member_id']
        self.config['ipb_pass_hash'] = config['ipb_pass_hash']
        self.config['ipb_session_id'] = config['ipb_session_id']
        self.config['igneous'] = config['igneous']
        self.config['sk'] = config['sk']
        # self.recv(self.config)
        self.recv("\n*** Cookies config Loaded. ***\n")
        self.hentai.build_config(self.config)
        self.rt.build_config(self.config, self.powers)

    def my_label_style(self, target, text):
        target.setText(text)
        target.setStyleSheet('color: green')

    def get_folder(self, path):
        self.folder = path

    def current_folder(self):
        os.startfile(self.folder)

    def open_folder(self):
        folder_name = QtWidgets.QFileDialog.getExistingDirectory(self,'Set dst folder')
        try:
            self.dst = folder_name+'/'
            self.ui.dst_text.setText(self.dst)
            self.hentai.build_dst(self.dst)

            # Check 0 bytes files
            self.recv('\n*** Checking if download failed images.. ***')
            self.ui.botton_folder.setEnabled(False)
            self.ui.botton_load_config.setEnabled(False)
            self.ui.botton_start.setEnabled(False)
            tags = os.listdir(self.dst)
            for tag in tags:
                path_tag = '{}{}'.format(self.dst, tag)
                if os.path.isdir(path_tag):
                    books = os.listdir(path_tag)
                    for book in books:
                        path_book = '{}{}/{}'.format(self.dst, tag, book)
                        if os.path.isdir(path_book):
                            imgs = os.listdir(path_book)
                            for img in imgs:
                                path = '{}{}/{}/{}'.format(self.dst, tag,book,img)
                                st = os.stat(path)
                                if st.st_size == 0:
                                    if '.JPG' in img:
                                        os.remove(path)
                                        print('{}{}/{}/{} has been removed!'.format(self.dst, tag,book,img))
                                        self.recv('{}{}/{}/{} has been removed!'.format(self.dst, tag,book,img))

            self.recv('\n*** Check Finish ***\n')
            self.ui.botton_folder.setEnabled(True)
            self.ui.botton_load_config.setEnabled(True)
            self.ui.botton_start.setEnabled(True)
        except:
            self.recv('\n*** Dst folder setting Error! ***\n')

    def put_tag(self, tag):
        self.ui.now_tag.setText(tag)

    def put_title(self, title):
        self.ui.label_title.setText(title)
        self.ui.label_title.setFont(QtGui.QFont("Times New Roman", 9, QtGui.QFont.Bold))
    
    def put_Cover(self, name):
        if (not os.path.isfile(name)) or (not os.stat(name).st_size !=0):
            name = self.last_image
        pixmap = QtGui.QPixmap(name)
        pixmap = pixmap.scaled(250,360,QtCore.Qt.KeepAspectRatio)
        self.ui.label_Cover.setPixmap(pixmap)
        image = np.array(Image.open(name))
        if image.shape == self.error_image.shape:
            if (image == self.error_image).all():
                self.recv('\n*** Error Image... ***\n')
                os.remove(name)
        self.last_image = name

    def put_book_config(self, config):
        self.ui.language.setText(config['language'][:-2])
        self.ui.parody.setText(config['parody'][:-2])
        self.ui.character.setText(config['character'][:-2])
        self.ui.artist.setText(config['artist'][:-2])
        self.ui.male.setText(config['male'][:-2])
        self.ui.female.setText(config['female'][:-2])
    
    def put_pages(self, page):
        self.my_label_style(self.ui.pages, page)
        self.ui.pages.setAlignment(QtCore.Qt.AlignRight)

    def recv(self, *args):
        for arg in args:
            if not isinstance(arg, str):
                arg = '{}'.format(arg)
            self.ui.message.append(arg)
            self.ui.message.moveCursor(self.ui.message.textCursor().End)

    def is_bad_conn(self):
        self.hentai.terminate()
        self.recv('\n*** Connect Failed !\n***Please Check Your Config !\n')

    def power(self, powers):
        self.powers = powers
        self.my_label_style(self.ui.power, powers)
        power = powers.split('/')
        now = int(power[0])
        limit = int(power[1])
        last = limit - now
        if last<=500 and limit!=0:
            if not self.flag_pause:
                self.recv('\n* * * * * * * * * * * * * * * * * * * * * * * * ')
                self.recv('* * * Will Out of flow ... <@{}'.format(last))
                self.recv('* * * Just pause the program...')
                self.recv('* * * * * * * * * * * * * * * * * * * * * * * * \n')
                self.is_pause()
                self.rt.terminate()
                

    def is_memory(self, mem):
        self.memory = mem
    
    def is_pause(self):
        if self.flag_pause:
            self.flag_pause = 0
            self.memory['pause']=1
            self.hentai.build_mem(self.memory)
            self.hentai.start()
            self.ui.botton_pause.setText('Pause')
        else:
            self.flag_pause = 1
            self.hentai.terminate()
            # self.recv(self.memory)
            self.ui.botton_pause.setText('Resume')
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = Main_Window()
    mw.show()
    sys.exit(app.exec_())