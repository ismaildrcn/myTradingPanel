from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QDesktopWidget, QGraphicsDropShadowEffect
from templates.ui.popup import Ui_Form


class MESSAGES():
    # message code 100+
    SUCCESSFUL = {
        1: 'Sembol başarılı bir şekilde eklendi.',
    }
    # message code 200+
    ERROR = {
        1: 'Sembol eklemede bir hata oluştu lütfen bilgileri kontrol ediniz!',
        2: 'Lütfen tüm alanları dolduğunuzdan emin olun!'
    }


class Popup(QDialog, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.central_show()
        self.setupUi(self)
        self.pushButton_ok.clicked.connect(self.ok_clicked)
        self.pushButton_cancel.clicked.connect(self.cancel_clicked)
        self.pushButton_ok.hide()
        self.pushButton_cancel.hide()

        self.add_shadow()

    def add_shadow(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)  # Gölgenin bulanıklık yarıçapını ayarlayın (isteğe bağlı)
        shadow.setColor(Qt.black)  # Gölge rengini ayarlayın (isteğe bağlı)
        shadow.setOffset(0, 0)

        self.widget_bg.setGraphicsEffect(shadow)

    def central_show(self):
        # Every time open Create Form in center display
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

    def showPopup(self, key):
        key_first = str(key)
        if key_first[0] == '1':
            message_key = key - 100
            self.setDesign(key_type='1')
            self.title.setText("BAŞARILI")
            self.message_code.setText(str(key))
            self.message.setText(MESSAGES.SUCCESSFUL[message_key])
        elif key_first[0] == '2':
            message_key = key - 200
            self.setDesign(key_type='2')
            self.title.setText("HATA")
            self.message_code.setText(str(key))
            self.message.setText(MESSAGES.ERROR[message_key])

    def setDesign(self, key_type):
        if key_type == '1':
            self.widget_status.setStyleSheet("#widget_status{\n"
                                             "background-color: rgb(43, 180, 39);\n"
                                             "border-radius:30px;\n"
                                             "}")
            self.status_icon.setPixmap(QtGui.QPixmap(':/images/templates/images/status-success-white.svg').scaled(150, 150))
            self.pushButton_ok.show()
            self.pushButton_cancel.hide()

        elif key_type == '2':
            self.widget_status.setStyleSheet("#widget_status{\n"
                                             "background-color: rgb(231, 24, 24);\n"
                                             "border-radius:30px;\n"
                                             "}")
            self.status_icon.setPixmap(QtGui.QPixmap(':/images/templates/images/status-error-white.svg').scaled(150, 150))
            self.pushButton_ok.hide()
            self.pushButton_cancel.show()

    def ok_clicked(self):
        self.close()

    def cancel_clicked(self):
        self.close()
