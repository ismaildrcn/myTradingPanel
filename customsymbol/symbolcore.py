from customsymbol.symbolview import SymbolView

class SymbolCore():
    def __init__(self, parent=None):
        self.symbolView = SymbolView(parent, parent.wallet_list)

        self._symbolClose = None
        self._symbolOpen = None
        self._symbolTime = None
        self._symbolName = None

    @property
    def symbolName(self):
        return self._symbolName

    @symbolName.setter
    def symbolName(self, value):
        self._symbolName = value
        self.symbolView.symbol_name.setText(str(self._symbolName))

    @property
    def symbolTime(self):
        return self._symbolTime

    @symbolTime.setter
    def symbolTime(self, value):
        self._symbolTime = value
        self.symbolView.label_symbol_update_time.setText(str(self._symbolTime))

    @property
    def symbolOpen(self):
        return self._symbolOpen

    @symbolOpen.setter
    def symbolOpen(self, value):
        self._symbolOpen = value
        self.symbolView.label_symbol_detail_1.setText(str(round(self._symbolOpen, 3)))

    @property
    def symbolClose(self):
        return self._symbolClose

    @symbolClose.setter
    def symbolClose(self, value):
        self._symbolClose = value
        self.symbolView.label_symbol_detail_2.setText(str(round(self._symbolClose, 3)))


class Symbol():
    def __init__(self, parent, name, detail):
        self.name = name

        self.time, self.open, self.close = detail

        self.symbolCore = SymbolCore(parent)
        self.symbolCore.symbolView.createSymbol()
        self.symbolCore.symbolName = self.name
        self.symbolCore.symbolTime = self.time.strftime("%H:%M:%S")
        self.symbolCore.symbolOpen = self.open
        self.symbolCore.symbolClose = self.close