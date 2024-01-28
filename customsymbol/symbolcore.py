from customsymbol.symbolview import SymbolView


class SymbolCore():
    def __init__(self, parent=None):
        self._parent = parent
        self._symbolClose = None
        self._symbolOpen = None
        self._symbolTime = None
        self._symbolName = None

    def setSymbolFrontend(self, c1, c2, c3):
        self._parent.symbolView.createSymbol()
        self.symbolName = c1
        self.symbolTime = 'None'
        self.symbolOpen = c2
        self.symbolClose = c3
        # self.symbolOpen = self.open
        # self.symbolClose = self.close

    @property
    def symbolName(self):
        return self._symbolName

    @symbolName.setter
    def symbolName(self, value):
        self._symbolName = value
        self._parent.symbolView.symbol_name.setText(str(self._symbolName))

    @property
    def symbolTime(self):
        return self._symbolTime

    @symbolTime.setter
    def symbolTime(self, value):
        self._symbolTime = value
        self._parent.symbolView.label_symbol_update_time.setText(str(self._symbolTime))

    @property
    def symbolOpen(self):
        return self._symbolOpen

    @symbolOpen.setter
    def symbolOpen(self, value):
        self._symbolOpen = value
        self._parent.symbolView.label_symbol_detail_1.setText(str(round(self._symbolOpen, 3)))

    @property
    def symbolClose(self):
        return self._symbolClose

    @symbolClose.setter
    def symbolClose(self, value):
        self._symbolClose = value
        self._parent.symbolView.label_symbol_detail_2.setText(str(round(self._symbolClose, 3)))


class Symbol:
    def __init__(self, name, cost, lot):
        self.name = name
        self.cost = cost  # maliyet
        self.lot = lot

        # self.symbolCore = SymbolCore(parent)
        # self.symbolCore.symbolView.createSymbol()
        # self.symbolCore.symbolName = name
        # self.symbolCore.symbolTime = 'None'
        # self.symbolCore.symbolOpen = cost
        # self.symbolCore.symbolClose = lot
        # self.symbolCore.symbolOpen = self.open
        # self.symbolCore.symbolClose = self.close

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        self._cost = float(value)

    @property
    def lot(self):
        return self._lot

    @lot.setter
    def lot(self, value):
        self._lot = float(value)
