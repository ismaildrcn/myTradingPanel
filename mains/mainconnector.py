from PyQt5.QtWidgets import QMainWindow
from templates.ui.mainWindow import Ui_MainWindow
from customsymbol.symbolhandler import SymbolHandler
from database.databaseconnector import Database
from popup.popup import Popup


class MainConnector(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.previousTitleIndex = None
        self.menu_status = None
        self.setupUi(self)
        self.symbolHandler = SymbolHandler(self)
        self.database = Database()
        self.popup = Popup()
        symbol_list = ['asd', 'BOBET', 'REEDR', 'BINHO', 'TABGD', 'THYAO']
        self.connection()
        self.initialize()
        self.show()

        # for item in symbol_list:
        #     Symbol(self, item, self.getSymbol.get_symbol(item, 'turkey', 'bist'))

    def connection(self):
        self.menu_pushButton_home_l.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.menu_pushButton_home_s.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.menu_pushButton_add_symbol_l.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.menu_pushButton_add_symbol_s.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_add_symbol_in.clicked.connect(lambda: self.stackedWidget_symbol.setCurrentIndex(0))
        self.pushButton_edit_symbol_in.clicked.connect(lambda: self.stackedWidget_symbol.setCurrentIndex(1))
        self.pushButton_add_symbol.clicked.connect(self.symbolHandler.symbolRealtime.addSymbol)
        self.menu_pushButton.clicked.connect(self.setMenu)

        self.stackedWidget.currentChanged.connect(self.stackedWidgetCurrentChanged)
        self.comboBox.currentIndexChanged.connect(self.symbolHandler.prepare_home_page)
        self.comboBox_2.currentIndexChanged.connect(self.symbolHandler.prepare_home_page)
        self.comboBox_3.currentIndexChanged.connect(self.symbolHandler.prepare_home_page)

    def stackedWidgetCurrentChanged(self, index):
        if index == 0 and not self.previousTitleIndex == index:
            self.title.setText('anasayfa'.upper())
            self.symbolHandler.prepare_home_page()
        elif index == 1 and not self.previousTitleIndex == index:
            self.title.setText('sembol ekle'.upper())
        self.previousTitleIndex = index

    def initialize(self):
        self.menu_pushButton_home_l.setVisible(False)
        self.menu_pushButton_add_symbol_l.setVisible(False)
        self.menu_status = False
        self.comboBox.setCurrentText('Taban')
        self.comboBox_2.setCurrentText('Tavan')
        self.comboBox_3.setCurrentText('Kar')

    def setMenu(self):
        if self.menu_status:
            self.setMenuAsSmall()
        else:
            self.setMenuAsLarge()

    def setMenuAsLarge(self):
        self.menu_pushButton_home_l.setVisible(True)
        self.menu_pushButton_add_symbol_l.setVisible(True)
        self.menu_status = True

    def setMenuAsSmall(self):
        self.menu_pushButton_home_l.setVisible(False)
        self.menu_pushButton_add_symbol_l.setVisible(False)
        self.menu_status = False

    def showMessagePopup(self, key):
        self.popup.showPopup(key)
        self.popup.show()


# hisselerin db den çekilmesi sağlandı seçili colonlara göre row verileri düzenlenecek. Handler üzerinden devam et