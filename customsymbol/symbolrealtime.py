from tradingview_ta import TA_Handler, Interval, TradingView


class SymbolRealtime():
    def __init__(self, parent=None):
        self._parent = parent

    def getSymbol(self, symbol, screener, exchange):
        try:
            sml = TA_Handler(
                symbol=symbol.upper(),
                screener=screener.lower(),
                exchange=exchange.upper(),
                interval=Interval.INTERVAL_1_DAY,
            )
            analysis = sml.get_analysis()
            return analysis.time, analysis.indicators['open'], analysis.indicators['close']
        except Exception as e:
            return False

    def addSymbol(self):
        if (
                not self._parent.lineEdit_symbol_name.text() == '' and
                not self._parent.lineEdit_symbol_exchange.text() == '' and
                not self._parent.lineEdit_symbol_cost.text() == '' and
                not self._parent.lineEdit_symbol_lot.text() == '' and
                not self._parent.comboBox_symbol_screener.currentText() == ''
        ):
            if self.getSymbol(
                    symbol=self._parent.lineEdit_symbol_name.text(),
                    screener=self._parent.comboBox_symbol_screener.currentText(),
                    exchange=self._parent.lineEdit_symbol_exchange.text()
            ):
                self._parent.database.addSymbol(
                    symbol=self._parent.lineEdit_symbol_name.text().upper(),
                    screener=self._parent.comboBox_symbol_screener.currentText().upper().lower(),
                    exchange=self._parent.lineEdit_symbol_exchange.text().upper(),
                    cost=float(self._parent.lineEdit_symbol_cost.text()),
                    lot=float(self._parent.lineEdit_symbol_lot.text())
                )
                self._parent.showMessagePopup(key=101)
            else:
                self._parent.showMessagePopup(key=201)
        else:
            self._parent.showMessagePopup(key=202)
