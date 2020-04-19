# coding=UTF-8

import os
import sys
import json
import time
import logging
import requests
from PyQt5 import QtCore
from bs4 import BeautifulSoup

class thread(QtCore.QThread):
    """
    Main Class PyQt.Thread
    """

    msg = QtCore.pyqtSignal(str)
    now_tag = QtCore.pyqtSignal(str)
    now_book = QtCore.pyqtSignal(str)
    now_page = QtCore.pyqtSignal(str)
    book_config = QtCore.pyqtSignal(dict)
    image = QtCore.pyqtSignal(str)
    memory = QtCore.pyqtSignal(dict)
    folder = QtCore.pyqtSignal(str)
    bad = QtCore.pyqtSignal(str)

    def __init__(self):
        """
        Initial parameter
        """
        super().__init__()

        self.homepage = 'https://exhentai.org/favorites.php?favcat=0'
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
        self.cookie = None
        self._log_init(logging.DEBUG)

        self.mem = {
            'favs':[],
            'fav_tabs':[],
            'books':[],
            'images':[],
            }
    
    def _log_init(self, level):
        """
        Create Logging
        """

        self.logger = logging.getLogger('logger')
        formatter = logging.Formatter("[%(asctime)s] %(levelname)s %(lineno)d: %(message)s")

        console1 = logging.StreamHandler()

        if os.path.isfile(os.getcwd()+'/test.log'):
            os.remove(os.getcwd()+'/test.log')
            
        console2 = logging.FileHandler(filename=os.getcwd()+'/test.log', encoding='utf-8')

        self.logger.setLevel(logging.DEBUG)
        console1.setLevel(level)
        console2.setLevel(logging.DEBUG)

        console1.setFormatter(formatter)
        console2.setFormatter(formatter)
        self.logger.addHandler(console1)
        self.logger.addHandler(console2)

    def event(self, e):
        """
        Crash event log
        """

        import traceback

        error_class = e.__class__.__name__ 
        detail = e.args[0]

        return '[{}] {}'.format(error_class, detail)

    def build_config(self, config):
        """
        Get cookies data from MainWindow
        """

        self.cookie = config

    def build_dst(self, dsts):
        """
        Get Dst from MainWindow
        """

        self.dst = dsts

    def build_mem(self,mem):
        """
        Get Memory of download list from MainWindow
        """

        self.mem = mem

    def request(self, url, content=False):
        """
        Request function;
        # url : url of website
        # content : content or not
        """
        
        time.sleep(1)

        if content:
            try:
                data = requests.get(url, cookies=self.cookie, headers={'User-Agent':self.user_agent})
            except Exception as e:
                self.msg.emit(self.event(e))
                self.logger.warning(self.event(e))
            else:
                return data
        else:
            try:
                resqonse = requests.get(url, cookies=self.cookie, headers={'User-Agent':self.user_agent})
            except Exception as e:
                self.msg.emit(self.event(e))
                self.logger.critical(self.event)
            else:
                soup = BeautifulSoup(resqonse.text, 'lxml')
                if len(soup) != 0:
                    return soup
                else:
                    self.bad.emit('False')
                    self.logger.debug('False')

    def _check_word(self, msg):
        """
        Replace unveiled word.
        """

        val =['\\','/',':','*','?','\"','<','>','|','?']

        for i,w in enumerate(msg):

            if w in val:

                msg = msg.replace(w, '_')

        return msg
    
    def _mkdir(self, dst):
        """
        Create folder, if target does not exist.
        """

        if not os.path.isdir(dst):

            self.logger.info('Create {} folder...'.format(dst))

            self.msg.emit('Create {} folder...'.format(dst))

            os.mkdir(dst)

        else:

            self.logger.info('{} is exited...'.format(dst))
            
            self.msg.emit('{} is exited...'.format(dst))

    def _is_lost(self,dst, pages):
        """
        Check pages of book lost or not.
        1. Check existed pages are larger than real pages of book or equal to real pages of book.
        2. List the number of all pages.
        3. Compare the set list.
        # dst : Dst folder
        # pages : real pages of book
        # return lost pages list.
        """

        lost = []
        lost_items=[]
        pages = int(pages) if not isinstance(pages, int) else pages

        filse = os.listdir(dst)

        if len(filse) >= pages:

            self.msg.emit('Downloaded!')
            self.logger.info('Downloaded !')

        else:

            f = set([int(x.split('.')[0]) for x in filse])
            p = set(list(range(1,pages+1)))

            lost_items = list(p.difference(f))

            for i in range(int(pages/20)+1):

                lost.append([])

            if pages%20 ==0:

                lost.pop()

            for i in range(1,pages+1):

                if i in lost_items:

                    page=int(i%20)
                    tab=int(i/20)

                    if page==0:

                        lost[tab-1].append(20)

                    else:

                        lost[tab].append(page)
        
        return lost, lost_items

    def _get_book_config(self, soup):
        """
        Get book config.
        """

        aaa = soup.select('div div div table')[-1]
        aa = aaa.find_all('a')
        config = {
            'language':'',
            'parody':'',
            'character':'',
            'artist':'',
            'male':'',
            'female':''
            }

        ma_1 = ''
        ma_2 = '\n'
        ma_3 = '\n'
        fm_1 = ''
        fm_2 = '\n'
        fm_3 = '\n'

        for a in aa:

            ele = str(a)

            if 'ta_language' in ele:
                
                config['language'] += '{}, '.format(a.text)

            elif 'ta_parody' in ele:

                if (len(config['parody']) + len(a.text)) > 80:

                    config['parody'] += '\n'

                config['parody'] += '{}, '.format(a.text)

            elif 'ta_character' in ele:

                if (len(config['character']) + len(a.text)) > 80:

                    config['character'] += '\n'

                config['character'] += '{}, '.format(a.text)

            elif 'ta_artist' in ele:

                config['artist'] += '{}, '.format(a.text)

            elif 'ta_male' in ele:

                if len(ma_1 + a.text) < 80:

                    ma_1 += '{}, '.format(a.text)

                elif len(ma_2 + a.text) < 80:

                    ma_2 += '{}, '.format(a.text)

                else:

                    ma_3 += '{}, '.format(a.text)

            elif 'ta_female' in ele:

                if len(fm_1 + a.text) < 80:

                    fm_1 += '{}, '.format(a.text)

                elif len(ma_2 + a.text) < 80:

                    fm_2 += '{}, '.format(a.text)

                else:

                    fm_3 += '{}, '.format(a.text)

        config['male'] = '{m1}{m2}{m3}'.format(m1=ma_1, m2=ma_2, m3=ma_3)
        config['female'] = '{m1}{m2}{m3}'.format(m1=fm_1, m2=fm_2, m3=fm_3)
        self.book_config.emit(config)

    def run(self):
        """
        Main running part.
        """

        soup_main = self.request('https://exhentai.org/favorites.php')

        favs = self._get_favs(soup_main) if len(self.mem['favs'])==0 else self.mem['favs']
        self.mem['favs'] = favs
        self.memory.emit(self.mem)

        self.logger.debug('Favorite has {f} tabs.'.format(f=len(self.mem['favs'])))
        while len(self.mem['favs']) != 0:

            self.fav = self.mem['favs'][0]
            self.fav_name = self.fav['title']
            self.fav_link = self.fav['link']
            self.logger.debug('Now at [{fav}]'.format(fav=self.fav_name))
            self.now_tag.emit(self.fav_name)

            self._mkdir(self.dst + self.fav_name)

            fav_tabs = self._get_fav_pages(self.fav) if len(self.mem['fav_tabs'])==0 else self.mem['fav_tabs']
            self.mem['fav_tabs'] = fav_tabs
            self.memory.emit(self.mem)
            self.logger.debug('[{fav}] has {tab} tabs'.format(fav=self.fav_name, tab=len(self.mem['fav_tabs'])))

            while len(self.mem['fav_tabs']) != 0:

                books = self._get_books(self.mem['fav_tabs']) if len(self.mem['books']) ==0 else self.mem['books']
                self.mem['books'] = books
                self.memory.emit(self.mem)
                self.logger.debug('[{fav}] has {book} books.'.format(fav=self.fav_name, book=len(self.mem['books'])))

                while len(self.mem['books']) != 0:

                    book = self.mem['books'][0]
                    self.book_name = book['title']
                    self.book_link = book['link']
                    self.book_pages = book['pages']
                    self.logger.debug('[{title}] has {page} pages.'.format(title=self.book_name, page=self.book_pages))
                    self.msg.emit('[{title}] has {page} pages.'.format(title=self.book_name, page=self.book_pages))
                    self.now_book.emit(self.book_name)

                    path = r'{dst}{now_fav}/{now_book}/'.format(dst=self.dst, now_fav=self.fav_name, now_book=self.book_name)
                    self.logger.debug('Checking {path} lost images or not ...'.format(path=path))
                    self._mkdir(path)
                    lost, lost_items = self._is_lost(path, self.book_pages)

                    if lost:

                        self.logger.info('{path} has lost {lost} images.'.format(path=path, lost=len(lost_items)))
                        soup = self.request(self.book_link)

                        try:
                            self._get_book_config(soup)
                            images = self._get_book_images(soup, lost, lost_items) if len(self.mem['images'])==0 else self.mem['images']
                            self.mem['images'] = images
                            self.memory.emit(self.mem)

                            if len(self.mem['images']) != 0:

                                self._get_images(self.mem['images'], self.book_pages)
                        except:
                            pass

                    self.mem['books'].pop(0)
                    self.memory.emit(self.mem)
                
                self.mem['fav_tabs'].pop(0)
                self.memory.emit(self.mem)

            self.mem['favs'].pop(0)
            self.memory.emit(self.mem)

        self.msg.emit("\n*** All Books have been Downloaded ! ***\n")

    def _get_favs(self, main_soup):
        """
        Get favorite tabs, save url and title.
        """

        favs = []

        host = 'https://exhentai.org/favorites.php?favcat='
        results = list(main_soup.find_all(class_='i'))

        if len(results) != 0:

            favs = [{'title':self._check_word(x['title']), 'link':host+str(i)} for i,x in enumerate(results)]
            
            self.logger.info('Favorite Urls get!')
        
        else:

            self.logger.error('Favorite Urls get Failed ...')
        
        return favs

    def _get_fav_pages(self, fav):
        """
        Get pages numbers of per favorite tab.
        """

        name_fav = fav['title']
        url_fav  = fav['link']
        f = url_fav[-1]
        url_fav_tabs = []

        soup = self.request(url_fav)

        if len(soup) != 0:
            
            try:

                pages_fav = int([x.text for x in soup.find(class_='ptt').select('a')][-2])

            except:

                pages_fav = 1

            self.logger.debug('[Fav: {title_fav}]: Pages: {pages_fav}'.format(title_fav=name_fav, pages_fav=pages_fav))
            url_fav_tabs = ['https://exhentai.org/favorites.php?page={n_fav_page}&favcat={n_fav}'.format(n_fav_page=x, n_fav=f) for x in range(pages_fav)]
        
        else:

            self.logger.error('[Fav: {title_fav}] could not get page data ...'.format(title_fav=name_fav))
        
        return url_fav_tabs
    
    def _get_books(self, url_fav_tabs):
        """
        Get books per favorite tab.
        """
        
        books = []

        for ft, fav_tab in enumerate(url_fav_tabs):

            soup = self.request(fav_tab)

            if len(soup) != 0:

                results = soup.select('.gl1t')

                for r in results:

                    link = r.find('a')['href']
                    title = r.find(class_='glink').text
                    pages = r.find(class_='gl5t').find('div').next_sibling.find('div').next_sibling.text

                    books.append({'title':self._check_word(title),
                                'link':link,
                                'pages':pages.split()[0]})
                    self.logger.debug('[{title}] : {p}'.format(title=self._check_word(title), p=pages))

        self.logger.debug('From Favorite get {n_books} books !'.format(n_books=len(books)))

        return books

    def _get_book_images(self, soup, lost, lost_items):
        """
        Get images link of book per books.
        If the image is in lost list, which will be downloaded.
        """

        images = []

        if len(soup) != 0:

            try:

                tabs = int([x.text for x in soup.find(class_='ptt').select('a')][-2])

            except:

                tabs = 1

            self.logger.debug('{title} has {nt} tabs and {np} pages'.format(title=self.book_name, nt=tabs, np=self.book_pages))
            book_tab_links = ['{host}?p={n}'.format(host=self.book_link, n=n) for n in range(tabs)]

            for t, tab in enumerate(book_tab_links):

                if lost[t] != 0:

                    tab_soup = soup if t==0 else self.request(tab)

                    if len(tab_soup) != 0:

                        for child in tab_soup.select('.gdtl'):

                            if int(child.find('img')['alt']) in lost_items:

                                host = child.find('a')['href']
                                ids  = child.find('img')['alt']

                                images.append({'host':host,
                                            'ids':ids})
        
        return images

    def _get_images(self, images, pages):
        """
        Download per images.
        """

        path = '{dst}{fav}/{book}/'.format(dst=self.dst, fav=self.fav_name, book=self.book_name)
        self.folder.emit(path)

        init = int(pages) - len(images)
        
        i=0
        while len(images) != 0:

            image = images[0]

            msg = '{now} / {total}'.format(now=i+1+init, total=pages)
            
            soup = self.request(image['host'])

            if len(soup) != 0:

                self.now_page.emit(msg)

                link = soup.select('#img')[0]['src']

                path_img = path + '{id}.JPG'.format(id=image['ids'])

                self._download(link, path_img)
                self.msg.emit(' - Download {book}_{id}'.format(book=self.book_name, id=image['ids']))
                self.image.emit(path_img)
            i+=1
            self.mem['images'].pop(0)
            self.memory.emit(self.mem)

    def _download(self, link, dst):
        """
        Download.
        """

        try:
            soup = self.request(link, content=True)

            with open(dst, 'wb') as f:

                f.write(soup.content)
            
            # break

        except Exception as e:
            error = self.event(e)
            
            self.msg.emit(error)
            self.logger.error(error)

if __name__ == "__main__":

    t = thread()
    t.debug()
