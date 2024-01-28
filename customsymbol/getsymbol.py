from tradingview_ta import TA_Handler, Interval, TradingView


class GetSymbol():
    def __init__(self):
        pass

    def get_symbol(self, symbol, screener, exchange):
        try:
            sml = TA_Handler(
                symbol=symbol.upper(),
                screener=screener.lower(),
                exchange=exchange.upper(),
                interval=Interval.INTERVAL_1_DAY,
            )
            analysis = sml.get_analysis()
            return (analysis.time, analysis.indicators['open'], analysis.indicators['close'])
        except Exception as e:
            return False
