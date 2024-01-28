from PyQt5.QtWidgets import QMainWindow
from templates.ui.mainWindow import Ui_MainWindow
from customsymbol.symbolcore import Symbol
from customsymbol.getsymbol import GetSymbol
from database.databaseconnector import Database
from popup.popup import Popup


class MainConnector(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.previousTitleIndex = None
        self.menu_status = None
        self.setupUi(self)
        self.getSymbol = GetSymbol()
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
        self.pushButton_add_symbol.clicked.connect(self.addSymbol)
        self.menu_pushButton.clicked.connect(self.setMenu)

        self.stackedWidget.currentChanged.connect(self.stackedWidgetCurrentChanged)

    def addSymbol(self):
        if (
                not self.lineEdit_symbol_name.text() == '' and
                not self.lineEdit_symbol_exchange.text() == '' and
                not self.lineEdit_symbol_cost.text() == '' and
                not self.lineEdit_symbol_lot.text() == '' and
                not self.comboBox_symbol_screener.currentText() == ''
        ):
            if self.getSymbol.get_symbol(
                    symbol=self.lineEdit_symbol_name.text(),
                    screener=self.comboBox_symbol_screener.currentText(),
                    exchange=self.lineEdit_symbol_exchange.text()
            ):
                self.database.addSymbol(
                    symbol=self.lineEdit_symbol_name.text().upper(),
                    screener=self.comboBox_symbol_screener.currentText().upper().lower(),
                    exchange=self.lineEdit_symbol_exchange.text().upper(),
                    cost=float(self.lineEdit_symbol_cost.text()),
                    lot=float(self.lineEdit_symbol_lot.text())
                )
                self.showMessagePopup(key=101)
            else:
                self.showMessagePopup(key=201)
        else:
            self.showMessagePopup(key=202)

    def stackedWidgetCurrentChanged(self, index):
        if index == 0 and not self.previousTitleIndex == index:
            self.title.setText('anasayfa'.upper())
        elif index == 1 and not self.previousTitleIndex == index:
            self.title.setText('sembol ekle'.upper())
        self.previousTitleIndex = index

    def initialize(self):
        self.menu_pushButton_home_l.setVisible(False)
        self.menu_pushButton_add_symbol_l.setVisible(False)
        self.menu_status = False

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
