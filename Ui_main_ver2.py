# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\ex_hentai\ver3\main_ver2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(800, 574)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Cover = QtWidgets.QLabel(self.centralwidget)
        self.label_Cover.setGeometry(QtCore.QRect(20, 10, 250, 360))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_Cover.setFont(font)
        self.label_Cover.setObjectName("label_Cover")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(280, 20, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label_title.setFont(font)
        self.label_title.setObjectName("label_title")
        self.label_language = QtWidgets.QLabel(self.centralwidget)
        self.label_language.setGeometry(QtCore.QRect(280, 70, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_language.setFont(font)
        self.label_language.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_language.setObjectName("label_language")
        self.language = QtWidgets.QLabel(self.centralwidget)
        self.language.setGeometry(QtCore.QRect(350, 70, 430, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.language.setFont(font)
        self.language.setObjectName("language")
        self.label_parody = QtWidgets.QLabel(self.centralwidget)
        self.label_parody.setGeometry(QtCore.QRect(280, 100, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_parody.setFont(font)
        self.label_parody.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_parody.setObjectName("label_parody")
        self.parody = QtWidgets.QLabel(self.centralwidget)
        self.parody.setGeometry(QtCore.QRect(350, 100, 430, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.parody.setFont(font)
        self.parody.setObjectName("parody")
        self.label_char = QtWidgets.QLabel(self.centralwidget)
        self.label_char.setGeometry(QtCore.QRect(270, 130, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_char.setFont(font)
        self.label_char.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_char.setObjectName("label_char")
        self.label_artist = QtWidgets.QLabel(self.centralwidget)
        self.label_artist.setGeometry(QtCore.QRect(280, 160, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_artist.setFont(font)
        self.label_artist.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_artist.setObjectName("label_artist")
        self.label_male = QtWidgets.QLabel(self.centralwidget)
        self.label_male.setGeometry(QtCore.QRect(280, 200, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_male.setFont(font)
        self.label_male.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_male.setObjectName("label_male")
        self.label_female = QtWidgets.QLabel(self.centralwidget)
        self.label_female.setGeometry(QtCore.QRect(280, 260, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_female.setFont(font)
        self.label_female.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_female.setObjectName("label_female")
        self.label_tags = QtWidgets.QLabel(self.centralwidget)
        self.label_tags.setGeometry(QtCore.QRect(280, 320, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_tags.setFont(font)
        self.label_tags.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_tags.setObjectName("label_tags")
        self.character = QtWidgets.QLabel(self.centralwidget)
        self.character.setGeometry(QtCore.QRect(350, 130, 430, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.character.setFont(font)
        self.character.setObjectName("character")
        self.artist = QtWidgets.QLabel(self.centralwidget)
        self.artist.setGeometry(QtCore.QRect(350, 160, 430, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.artist.setFont(font)
        self.artist.setObjectName("artist")
        self.male = QtWidgets.QLabel(self.centralwidget)
        self.male.setGeometry(QtCore.QRect(350, 200, 430, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.male.setFont(font)
        self.male.setObjectName("male")
        self.female = QtWidgets.QLabel(self.centralwidget)
        self.female.setGeometry(QtCore.QRect(350, 260, 430, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.female.setFont(font)
        self.female.setObjectName("female")
        self.now_tag = QtWidgets.QLabel(self.centralwidget)
        self.now_tag.setGeometry(QtCore.QRect(350, 320, 430, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.now_tag.setFont(font)
        self.now_tag.setObjectName("now_tag")
        self.message = QtWidgets.QTextBrowser(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(290, 380, 491, 151))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.message.setFont(font)
        self.message.setObjectName("message")
        self.botton_load_config = QtWidgets.QPushButton(self.centralwidget)
        self.botton_load_config.setGeometry(QtCore.QRect(20, 390, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.botton_load_config.setFont(font)
        self.botton_load_config.setIconSize(QtCore.QSize(64, 32))
        self.botton_load_config.setObjectName("botton_load_config")
        self.botton_start = QtWidgets.QPushButton(self.centralwidget)
        self.botton_start.setGeometry(QtCore.QRect(20, 440, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.botton_start.setFont(font)
        self.botton_start.setIconSize(QtCore.QSize(64, 32))
        self.botton_start.setObjectName("botton_start")
        self.botton_exit = QtWidgets.QPushButton(self.centralwidget)
        self.botton_exit.setGeometry(QtCore.QRect(150, 440, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.botton_exit.setFont(font)
        self.botton_exit.setIconSize(QtCore.QSize(64, 32))
        self.botton_exit.setObjectName("botton_exit")
        self.label_dst = QtWidgets.QLabel(self.centralwidget)
        self.label_dst.setGeometry(QtCore.QRect(280, 352, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_dst.setFont(font)
        self.label_dst.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_dst.setObjectName("label_dst")
        self.dst_text = QtWidgets.QLineEdit(self.centralwidget)
        self.dst_text.setGeometry(QtCore.QRect(350, 350, 350, 20))
        self.dst_text.setObjectName("dst_text")
        self.botton_folder = QtWidgets.QPushButton(self.centralwidget)
        self.botton_folder.setGeometry(QtCore.QRect(710, 350, 30, 20))
        self.botton_folder.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/cover/folder_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botton_folder.setIcon(icon)
        self.botton_folder.setIconSize(QtCore.QSize(14, 14))
        self.botton_folder.setObjectName("botton_folder")
        self.label_pages = QtWidgets.QLabel(self.centralwidget)
        self.label_pages.setGeometry(QtCore.QRect(150, 410, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_pages.setFont(font)
        self.label_pages.setObjectName("label_pages")
        self.pages = QtWidgets.QLabel(self.centralwidget)
        self.pages.setGeometry(QtCore.QRect(200, 410, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pages.setFont(font)
        self.pages.setObjectName("pages")
        self.botton_pause = QtWidgets.QPushButton(self.centralwidget)
        self.botton_pause.setGeometry(QtCore.QRect(20, 490, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.botton_pause.setFont(font)
        self.botton_pause.setObjectName("botton_pause")
        self.botton_open_folder = QtWidgets.QPushButton(self.centralwidget)
        self.botton_open_folder.setGeometry(QtCore.QRect(750, 350, 30, 20))
        self.botton_open_folder.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/cover/folder_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botton_open_folder.setIcon(icon1)
        self.botton_open_folder.setIconSize(QtCore.QSize(14, 14))
        self.botton_open_folder.setObjectName("botton_open_folder")
        self.label_power = QtWidgets.QLabel(self.centralwidget)
        self.label_power.setGeometry(QtCore.QRect(150, 390, 41, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_power.setFont(font)
        self.label_power.setObjectName("label_power")
        self.power = QtWidgets.QLabel(self.centralwidget)
        self.power.setGeometry(QtCore.QRect(200, 390, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.power.setFont(font)
        self.power.setObjectName("power")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ex-Hentai Auto-Downloader Ver.2"))
        self.label_Cover.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ff0000;\">NO</span></p><p align=\"center\"><span style=\" font-size:72pt; font-weight:600; color:#ff0000;\">DATA</span></p></body></html>"))
        self.label_title.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Title</span></p></body></html>"))
        self.label_language.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Language :</p></body></html>"))
        self.language.setText(_translate("MainWindow", "Language"))
        self.label_parody.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Parody :</p></body></html>"))
        self.parody.setText(_translate("MainWindow", "Parody"))
        self.label_char.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Character :</p></body></html>"))
        self.label_artist.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Artist :</p></body></html>"))
        self.label_male.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Male :</p></body></html>"))
        self.label_female.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Female :</p></body></html>"))
        self.label_tags.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Now tag :</p></body></html>"))
        self.character.setText(_translate("MainWindow", "Character"))
        self.artist.setText(_translate("MainWindow", "Artist"))
        self.male.setText(_translate("MainWindow", "<html><head/><body><p>male</p><p><br/></p><p><br/></p></body></html>"))
        self.female.setText(_translate("MainWindow", "<html><head/><body><p>female</p><p><br/></p><p><br/></p></body></html>"))
        self.now_tag.setText(_translate("MainWindow", "tags"))
        self.botton_load_config.setText(_translate("MainWindow", "Load Config"))
        self.botton_start.setText(_translate("MainWindow", "Start"))
        self.botton_exit.setText(_translate("MainWindow", "Exit"))
        self.label_dst.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Dst :</p></body></html>"))
        self.label_pages.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:10pt; font-weight:600;\">Pages :</span></p></body></html>"))
        self.pages.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-weight:400;\">pages</span></p></body></html>"))
        self.botton_pause.setText(_translate("MainWindow", "Pauese"))
        self.label_power.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\">Limit :</p></body></html>"))
        self.power.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-weight:400;\">0 / 0</span></p></body></html>"))
import cover_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
