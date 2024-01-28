from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QListWidgetItem, QFrame


class SeparatorItem(QFrame):
    def __init__(self):
        super().__init__()
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Sunken)


class SymbolView():
    def __init__(self, parent=None, widget=None):
        self._parent = parent
        self.widget = widget
        self.widget.setSpacing(3)

    def createSymbol(self):
        self.symbol_row1 = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.symbol_row1.sizePolicy().hasHeightForWidth())
        self.symbol_row1.setSizePolicy(sizePolicy)
        self.symbol_row1.setStyleSheet("#symbol_row1{\n"
                                       "    background-color: rgb(255, 255, 255);\n"
                                       "    border-radius: 12px;\n"
                                       "}")
        self.symbol_row1.setObjectName("symbol_row1")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.symbol_row1)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.widget_symbol_name = QtWidgets.QWidget(self.symbol_row1)
        self.widget_symbol_name.setObjectName("widget_symbol_name")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_symbol_name)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.symbol_name = QtWidgets.QLabel(self.widget_symbol_name)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.symbol_name.setFont(font)
        self.symbol_name.setObjectName("symbol_name")
        self.verticalLayout_5.addWidget(self.symbol_name)
        self.label_symbol_update_time = QtWidgets.QLabel(self.widget_symbol_name)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_symbol_update_time.setFont(font)
        self.label_symbol_update_time.setObjectName("label_symbol_update_time")
        self.verticalLayout_5.addWidget(self.label_symbol_update_time)
        self.horizontalLayout_8.addWidget(self.widget_symbol_name)
        self.widget_symbol_detail_column_1 = QtWidgets.QWidget(self.symbol_row1)
        self.widget_symbol_detail_column_1.setObjectName("widget_symbol_detail_column_1")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_symbol_detail_column_1)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_symbol_detail_1 = QtWidgets.QLabel(self.widget_symbol_detail_column_1)
        self.label_symbol_detail_1.setObjectName("label_symbol_detail_1")
        self.verticalLayout_6.addWidget(self.label_symbol_detail_1)
        self.horizontalLayout_8.addWidget(self.widget_symbol_detail_column_1)
        self.widget_symbol_detail_column_2 = QtWidgets.QWidget(self.symbol_row1)
        self.widget_symbol_detail_column_2.setObjectName("widget_symbol_detail_column_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_symbol_detail_column_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_symbol_detail_2 = QtWidgets.QLabel(self.widget_symbol_detail_column_2)
        self.label_symbol_detail_2.setObjectName("label_symbol_detail_2")
        self.verticalLayout_7.addWidget(self.label_symbol_detail_2)
        self.horizontalLayout_8.addWidget(self.widget_symbol_detail_column_2)
        self.widget_symbol_detail_column_3 = QtWidgets.QWidget(self.symbol_row1)
        self.widget_symbol_detail_column_3.setObjectName("widget_symbol_detail_column_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget_symbol_detail_column_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_symbol_detail_3 = QtWidgets.QLabel(self.widget_symbol_detail_column_3)
        self.label_symbol_detail_3.setObjectName("label_symbol_detail_3")
        self.verticalLayout_8.addWidget(self.label_symbol_detail_3)
        self.horizontalLayout_8.addWidget(self.widget_symbol_detail_column_3)


        item = QListWidgetItem()
        item.setSizeHint(self.symbol_row1.sizeHint())
        self.widget.addItem(item)
        self.widget.setItemWidget(item, self.symbol_row1)

        separator_item = QListWidgetItem()
        separator_item.setSizeHint(QSize(1, 1))  # Yüksekliği 1 piksel
        separator_item.setBackground(QBrush(QColor(0, 0, 0, 50)))  # Siyah renk için QBrush kullanıldı
        self.widget.addItem(separator_item)



