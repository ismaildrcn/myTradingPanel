from customsymbol.symbolcore import Symbol
from customsymbol.symbolrealtime import SymbolRealtime
from customsymbol.symbolcore import SymbolCore
from customsymbol.symbolview import SymbolView


class SymbolHandler():
    def __init__(self, parent=None):
        self._parent = parent
        self.symbolView = SymbolView(self._parent, self._parent.wallet_list)
        self.symbolCore = SymbolCore(self)
        self.symbolRealtime = SymbolRealtime(self._parent)


        self._symbols = []

    def prepare_home_page(self):
        self._parent.wallet_list.clear()
        self._symbols.clear()
        symbols = self._parent.database.getAllSymbols()
        for symbol in symbols:
            time, open, close = self.symbolRealtime.getSymbol(symbol=symbol[1], screener=symbol[2], exchange=symbol[3])
            print("Time: {}, Open: {}, Close: {}, Cost: {}, Lot: {}".format(time, open, close, symbol[4], symbol[5]))
            item = Symbol(symbol[1], symbol[4], symbol[5])
            self._symbols.append(item)

            c1, c2, c3 = self.getComboBoxValues()
            if c1.lower() == 'tavan':
                r1 = open * 1.1
            else:
                r1 = open
            if c2.lower() == 'taban':
                r2 = open / 1.1
            else:
                r2 = open
            if c3.lower() == 'kar':
                r3 = close * symbol[5]
            else:
                r3 = close
        for symbol in self._symbols:
            self.symbolCore.setSymbolFrontend(
                symbol.name,
                symbol.cost,
                symbol.lot
            )
            # self.createSymbol(symbol[1], r2, r3)


    def getComboBoxValues(self):
        return self._parent.comboBox.currentText(), self._parent.comboBox_2.currentText(), self._parent.comboBox_3.currentText()